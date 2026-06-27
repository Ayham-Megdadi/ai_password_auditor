#!/usr/bin/env python3
"""
╔══════════════════════════════════════════════════════╗
║          AI PASSWORD AUDITOR — v2.0                 ║
║      Developed by: Ayham Belal Megdadi              ║
║      For Educational & Ethical Use Only             ║
╚══════════════════════════════════════════════════════╝
"""

import sys
import os
import re
import json
import math
import hmac
import hashlib
import getpass
import argparse
from datetime import datetime


class C:
    RESET  = "\033[0m"
    BOLD   = "\033[1m"
    DIM    = "\033[2m"
    RED    = "\033[91m"
    YELLOW = "\033[93m"
    GREEN  = "\033[92m"
    CYAN   = "\033[96m"
    BLUE   = "\033[94m"
    WHITE  = "\033[97m"

def col(color, text):
    if sys.stdout.isatty():
        return f"{color}{text}{C.RESET}"
    return text


BANNER = f"""
{col(C.CYAN, C.BOLD)}
 █████╗ ██╗    ██████╗  █████╗ ███████╗███████╗
██╔══██╗██║    ██╔══██╗██╔══██╗██╔════╝██╔════╝
███████║██║    ██████╔╝███████║███████╗███████╗
██╔══██║██║    ██╔═══╝ ██╔══██║╚════██║╚════██║
██║  ██║██║    ██║     ██║  ██║███████║███████║
╚═╝  ╚═╝╚═╝    ╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝
{C.RESET}
{col(C.CYAN, '         AI PASSWORD AUDITOR  v2.0')}
{col(C.DIM,  '     Developed by: Ayham Belal Megdadi')}
{col(C.DIM,  '       Educational & Ethical Use Only')}
"""


COMMON_PASSWORDS = {
    "123456", "password", "admin", "12345678", "user", "letmein",
    "qwerty", "abc123", "111111", "iloveyou", "1234567890", "test",
    "login", "welcome", "monkey", "dragon", "master", "sunshine",
    "princess", "shadow", "123123", "pass", "root", "toor",
}


PATTERNS = [
    (r"(.)\1{2,}",              "Repeated characters detected"),
    (r"(012|123|234|345|456|567|678|789|890|901)", "Sequential digits detected"),
    (r"(abc|bcd|cde|def|efg|fgh|ghi|hij|ijk|jkl|klm|lmn|mno|nop|opq|pqr|qrs|rst|stu|tuv|uvw|vwx|wxy|xyz)",
                                "Sequential letters detected"),
    (r"(qwerty|asdf|zxcv|qazwsx|1qaz|2wsx)", "Keyboard pattern detected"),
    (r"^\d+$",                  "Digits only — very predictable"),
    (r"^[a-zA-Z]+$",            "Letters only — no symbols or digits"),
]


def calc_entropy(pwd: str) -> float:
    """Shannon entropy in bits per character × length."""
    charset = 0
    if any(c.islower() for c in pwd):   charset += 26
    if any(c.isupper() for c in pwd):   charset += 26
    if any(c.isdigit() for c in pwd):   charset += 10
    if any(c in "!@#$%^&*()-_=+[{]};:'\",<.>/?\\|`~ " for c in pwd): charset += 32
    if charset == 0:
        return 0.0
    return round(len(pwd) * math.log2(charset), 2)


def audit_password(pwd: str, username: tuple = (), birth_year: str = "") -> dict:
    """
    Returns a detailed audit dict with score, strength, entropy,
    pattern warnings, and actionable suggestions.
    """
    score       = 0
    warnings    = []
    suggestions = []

    length = len(pwd)
    if length >= 16:
        score += 2
    elif length >= 12:
        score += 1.5
    elif length >= 8:
        score += 1
    else:
        warnings.append("Too short (minimum 8 characters recommended)")
        suggestions.append("Use at least 12–16 characters for strong security")

    has_upper  = any(c.isupper() for c in pwd)
    has_lower  = any(c.islower() for c in pwd)
    has_digit  = any(c.isdigit() for c in pwd)
    has_symbol = any(c in "!@#$%^&*()-_=+[{]};:'\",<.>/?\\|`~" for c in pwd)

    if has_upper and has_lower:
        score += 1
    else:
        suggestions.append("Mix uppercase and lowercase letters")

    if has_digit:
        score += 1
    else:
        suggestions.append("Add at least one digit")

    if has_symbol:
        score += 1.5
    else:
        suggestions.append("Add special characters (!@#$%^&*...)")

    if pwd.lower() in COMMON_PASSWORDS:
        score -= 3
        warnings.append("This password appears in known breach lists!")
        suggestions.append("Choose a completely different password")

    for u in username:
        if u and u.lower() in pwd.lower():
            score -= 1
            warnings.append(f"Password contains username '{u}'")
            suggestions.append("Never include your username in your password")
            break

    if birth_year and birth_year in pwd:
        score -= 1
        warnings.append("Password contains your birth year")
        suggestions.append("Avoid personal info like birth years")

    for pattern, msg in PATTERNS:
        if re.search(pattern, pwd, re.IGNORECASE):
            score -= 0.5
            warnings.append(msg)

    entropy = calc_entropy(pwd)
    if entropy >= 60:
        score += 1
    elif entropy < 30:
        warnings.append(f"Low entropy ({entropy} bits) — easy to brute-force")

    score = max(0, score)

    if score <= 2:
        strength = "Weak"
        color    = C.RED
    elif score <= 4:
        strength = "Medium"
        color    = C.YELLOW
    elif score <= 6:
        strength = "Strong"
        color    = C.GREEN
    else:
        strength = "Very Strong"
        color    = C.CYAN

    return {
        "password":    pwd,
        "score":       round(score, 1),
        "strength":    strength,
        "color":       color,
        "entropy":     entropy,
        "length":      length,
        "has_upper":   has_upper,
        "has_lower":   has_lower,
        "has_digit":   has_digit,
        "has_symbol":  has_symbol,
        "warnings":    warnings,
        "suggestions": suggestions,
    }


def strength_bar(score: float, max_score: float = 8) -> str:
    filled = int((score / max_score) * 20)
    bar    = "█" * filled + "░" * (20 - filled)
    return bar

def print_audit(r: dict, show_password: bool = True):
    sep = col(C.DIM, "  " + "─" * 52)
    print()
    print(sep)
    if show_password:
        print(col(C.CYAN,  "  Password  : ") + col(C.BOLD, r["password"]))
    print(col(C.CYAN,  "  Strength  : ") + col(r["color"], col(C.BOLD, r["strength"])))
    print(col(C.CYAN,  "  Score     : ") + f"{r['score']}/8  {col(r['color'], strength_bar(r['score']))}")
    print(col(C.CYAN,  "  Entropy   : ") + f"{r['entropy']} bits")
    print(col(C.CYAN,  "  Length    : ") + str(r["length"]))

    flags = []
    flags.append(col(C.GREEN, "A-Z") if r["has_upper"]  else col(C.DIM, "A-Z"))
    flags.append(col(C.GREEN, "a-z") if r["has_lower"]  else col(C.DIM, "a-z"))
    flags.append(col(C.GREEN, "0-9") if r["has_digit"]  else col(C.DIM, "0-9"))
    flags.append(col(C.GREEN, "!@#") if r["has_symbol"] else col(C.DIM, "!@#"))
    print(col(C.CYAN,  "  Contains  : ") + "  ".join(flags))

    if r["warnings"]:
        print()
        for w in r["warnings"]:
            print(col(C.RED, f"  ⚠  {w}"))

    if r["suggestions"]:
        print()
        for s in r["suggestions"]:
            print(col(C.YELLOW, f"  ✦  {s}"))

    print(sep)
    print()


DEFAULT_LIST = [
    "123456", "password", "admin", "12345678", "user",
    "111222333!", "test", "ZXCdsaQWE@231", "A1b2C3!",
    "Jordan", "Strong_P@ss1", "A1b@C3d#", "PA@swo#2",
    "pAs!312", "Val1d_P@ssw0rd!",
]

def batch_audit(passwords: list, username=(), birth_year="", export_json=False):
    print(col(C.BOLD, f"\n  {'Password':<22} {'Score':>5}  {'Strength':<12} {'Entropy':>8}"))
    print(col(C.DIM,  "  " + "─" * 55))

    results = []
    for pwd in passwords:
        r = audit_password(pwd, username, birth_year)
        strength_colored = col(r["color"], f"{r['strength']:<12}")
        warn_icon = col(C.RED, " ⚠") if r["warnings"] else "  "
        print(f"  {pwd:<22} {r['score']:>5}  {strength_colored} {r['entropy']:>8} bits{warn_icon}")
        results.append(r)

    counts = {"Weak": 0, "Medium": 0, "Strong": 0, "Very Strong": 0}
    for r in results:
        counts[r["strength"]] = counts.get(r["strength"], 0) + 1

    print(col(C.DIM, "\n  " + "─" * 55))
    print(col(C.BOLD, "\n  Summary:"))
    for lvl, n in counts.items():
        bar = "■" * n
        print(f"    {lvl:<12}: {n:>3}  {bar}")

    if export_json:
        ts  = datetime.now().strftime("%Y%m%d_%H%M%S")
        out = f"audit_report_{ts}.json"
        clean = [{k: v for k, v in r.items() if k != "color"} for r in results]
        with open(out, "w") as f:
            json.dump({"generated": datetime.now().isoformat(), "results": clean}, f, indent=2)
        print(col(C.CYAN, f"\n  Report saved → {out}\n"))


import secrets
import string

def suggest_strong_password(length: int = 16) -> str:
    alphabet = string.ascii_letters + string.digits + "!@#$%^&*()-_=+"
    while True:
        pwd = "".join(secrets.choice(alphabet) for _ in range(length))
        r   = audit_password(pwd)
        if r["strength"] in ("Strong", "Very Strong"):
            return pwd


USERS = {
    "ayham": hashlib.sha256("admin".encode()).hexdigest(),
    "admin": hashlib.sha256("admin".encode()).hexdigest(),
}

def login() -> bool:
    print(col(C.CYAN, "\n  ── Authentication ──"))
    username = input(col(C.CYAN, "  Username : ")).strip().lower()
    password = getpass.getpass(col(C.CYAN, "  Password : "))
    hashed   = hashlib.sha256(password.encode()).hexdigest()

    if username in USERS and hmac.compare_digest(USERS[username], hashed):
        print(col(C.GREEN, f"\n  ✔ Welcome, {username}!\n"))
        return True

    print(col(C.RED, "\n  ✘ Authentication failed.\n"))
    return False


MENU = """
  ╔══════════════════════════════════════════╗
  ║           SELECT AN OPTION              ║
  ╠══════════════════════════════════════════╣
  ║  1)  Audit a single password            ║
  ║  2)  Run batch audit (built-in list)    ║
  ║  3)  Batch audit from file              ║
  ║  4)  Generate strong password           ║
  ║  5)  Exit                               ║
  ╚══════════════════════════════════════════╝"""

def interactive_mode():
    print(BANNER)
    if not login():
        sys.exit(1)

    username   = ("ayham", "admin", "user")
    birth_year = "2004"

    while True:
        print(MENU)
        choice = input(col(C.CYAN, "\n  Enter choice: ")).strip()

        if choice == "1":
            pwd = getpass.getpass(col(C.CYAN, "  Enter password to audit: "))
            r   = audit_password(pwd, username, birth_year)
            print_audit(r, show_password=False)

        elif choice == "2":
            export = input(col(C.CYAN, "  Export JSON report? [y/N]: ")).strip().lower() == "y"
            batch_audit(DEFAULT_LIST, username, birth_year, export_json=export)

        elif choice == "3":
            fp = input(col(C.CYAN, "  File path (one password per line): ")).strip()
            if not os.path.isfile(fp):
                print(col(C.RED, "  [!] File not found"))
                continue
            with open(fp) as f:
                pwds = [l.strip() for l in f if l.strip()]
            export = input(col(C.CYAN, "  Export JSON report? [y/N]: ")).strip().lower() == "y"
            batch_audit(pwds, username, birth_year, export_json=export)

        elif choice == "4":
            try:
                length = int(input(col(C.CYAN, "  Password length [16]: ")).strip() or "16")
            except ValueError:
                length = 16
            pwd = suggest_strong_password(length)
            print(col(C.GREEN, f"\n  ✔ Suggested: {col(C.BOLD, pwd)}\n"))
            r   = audit_password(pwd)
            print_audit(r)

        elif choice == "5":
            print(col(C.CYAN, "\n  Goodbye — stay secure.\n"))
            break

        else:
            print(col(C.RED, "\n  [!] Invalid option, try again."))


def build_parser():
    p = argparse.ArgumentParser(
        prog="AI-Password-Auditor",
        description="AI Password Auditor v2.0 — by Ayham Belal Megdadi",
    )
    sub = p.add_subparsers(dest="cmd")

    pa = sub.add_parser("audit", help="Audit a single password")
    pa.add_argument("password", help="Password string to audit")
    pa.add_argument("-u", "--username", nargs="*", default=[], help="Username(s) to check against")
    pa.add_argument("-b", "--birth",    default="",  help="Birth year to check against")

    pb = sub.add_parser("batch", help="Batch audit from file")
    pb.add_argument("filepath")
    pb.add_argument("--json", action="store_true", help="Export JSON report")

    sub.add_parser("generate", help="Generate a strong password")

    return p

def cli_mode():
    parser = build_parser()
    args   = parser.parse_args()

    if args.cmd == "audit":
        r = audit_password(args.password, tuple(args.username), args.birth)
        print_audit(r)

    elif args.cmd == "batch":
        if not os.path.isfile(args.filepath):
            print(col(C.RED, f"File not found: {args.filepath}"))
            sys.exit(1)
        with open(args.filepath) as f:
            pwds = [l.strip() for l in f if l.strip()]
        batch_audit(pwds, export_json=args.json)

    elif args.cmd == "generate":
        pwd = suggest_strong_password()
        print(col(C.GREEN, f"\nSuggested password: {col(C.BOLD, pwd)}"))
        r   = audit_password(pwd)
        print_audit(r)

    else:
        parser.print_help()


if __name__ == "__main__":
    if len(sys.argv) > 1:
        cli_mode()
    else:
        interactive_mode()
