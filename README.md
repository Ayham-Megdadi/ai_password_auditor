````markdown
<h1 align="center">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=26&pause=1000&color=00FF88&center=true&vCenter=true&width=700&lines=AI+Password+Auditor+v2.0;Entropy+%7C+Pattern+Detection+%7C+Security+Analysis;Built+by+Ayham+Belal+Megdadi" alt="Typing SVG"/>
</h1>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python"/>
  <img src="https://img.shields.io/badge/Version-2.0-brightgreen?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Security-Ethical%20Use-red?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Dependencies-Zero-orange?style=for-the-badge"/>
</p>

---

> **Developed by Ayham Belal Megdadi**  
> Educational & Ethical Use Only

---

# 🔐 AI Password Auditor

A Python command-line tool for auditing password strength using entropy analysis, pattern detection, breach-list checks, cryptographic scoring, and secure password generation.

Designed for cybersecurity students, penetration testers, and security professionals who want to evaluate password security using practical security metrics.

---

# ✨ Features

| Feature | Description |
|---------|-------------|
| 🔍 Password Audit | Analyze password strength with detailed scoring |
| 📐 Entropy Analysis | Estimate password randomness using Shannon entropy |
| 🧩 Pattern Detection | Detect sequential characters, repeated characters, keyboard patterns, and weak structures |
| 🚨 Breach List Check | Compare passwords against a built-in list of commonly leaked passwords |
| 👤 PII Detection | Warn when usernames or birth years appear inside passwords |
| 🔐 Secure Password Generator | Generate cryptographically secure passwords |
| 📊 Batch Audit | Audit multiple passwords from a text file |
| 📄 JSON Reports | Export audit results as JSON |
| 📈 Strength Meter | Visual strength bar with color-coded ratings |
| 🖥 Interactive & CLI Modes | Use the tool interactively or directly from the command line |
| 🔒 Secure Authentication | SHA-256 hashing with constant-time comparison |

---

# 🧠 How It Works

The auditor evaluates passwords across several security dimensions.

| Dimension | Description |
|-----------|-------------|
| 🔢 Length | Rewards passwords with 8, 12, and 16+ characters |
| 🔡 Character Variety | Checks uppercase, lowercase, digits, and symbols |
| 📐 Entropy | Calculates password randomness (Shannon entropy) |
| 🚨 Breach List | Detects common leaked passwords |
| 🧩 Weak Patterns | Finds sequential characters, repetition, keyboard walks, and predictable structures |
| 👤 Personal Information | Detects usernames and birth years inside passwords |

---

# ⚙️ Requirements

- Python 3.8+
- No external dependencies
- Cross-platform (Windows, Linux, macOS)

---

# 📦 Installation

```bash
git clone https://github.com/Ayham-Megdadi/ai_password_auditor.git

cd ai_password_auditor

python3 AI-Password-Auditor.py
````

---

# 🚀 Usage

## Interactive Mode

```bash
python3 AI-Password-Auditor.py
```

---

## Audit a Password

```bash
python3 AI-Password-Auditor.py audit "MyP@ssw0rd!" -u ayham -b 2004
```

---

## Batch Audit

```bash
python3 AI-Password-Auditor.py batch passwords.txt --json
```

---

## Generate a Strong Password

```bash
python3 AI-Password-Auditor.py generate
```

---

# 📋 Example Output

```text
Password  : admin

Strength  : Weak

Score     : 0/8
░░░░░░░░░░░░░░░░░░░░

Entropy   : 23.5 bits

⚠ Too short (minimum 8 characters)

⚠ Password found in common breach list

✦ Use at least 12–16 characters

✦ Add uppercase, digits, and symbols
```

---

# 📂 Project Structure

```
ai_password_auditor/
│
├── AI-Password-Auditor.py
├── README.md
├── LICENSE
├── SECURITY.md
└── .gitignore
```

---

# 🛡 Security

If you discover a security issue, please report it privately.

Please **do not** open a public issue for security vulnerabilities.

---

# ⚠️ Disclaimer

This project is intended **strictly for educational and ethical cybersecurity purposes**.

Do **not** use this tool to audit passwords that you do not own or do not have explicit permission to test.

The developer assumes no responsibility for misuse of this software.

---

# 📄 License

Released under the **MIT License**.

---

<p align="center">
Made with ❤️ by <strong>Ayham Belal Megdadi</strong>
</p>
```
