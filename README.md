<h1 align="center">
<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=26&pause=1000&color=00FF88&center=true&vCenter=true&width=700&lines=AI+Password+Auditor+v2.0;Entropy+%7C+Patterns+%7C+Breach+Detection;Built+by+Ayham+Belal+Megdadi" alt="Typing SVG"/>
</h1>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python"/>
  <img src="https://img.shields.io/badge/Version-2.0-brightgreen?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Security-Ethical%20Use-red?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Dependencies-Zero-orange?style=for-the-badge"/>
</p>

> **Developed by Ayham Belal Megdadi** — For Educational & Ethical Use Only

## How It Works

The auditor scores each password across 6 dimensions:

| Dimension | What it checks |
|---|---|
| 🔢 Length | 8 / 12 / 16+ characters |
| 🔡 Variety | Uppercase, lowercase, digits, symbols |
| 📐 Entropy | Bits of randomness (Shannon entropy) |
| 🚨 Breach List | Compared against 24 known leaked passwords |
| 🧩 Patterns | Keyboard walks, sequential chars, repetition |
| 👤 PII Check | Username and birth year in password |

## Features

| Feature | Description |
|---|---|
| ✅ Single Audit | Deep analysis of one password with warnings |
| 📊 Batch Audit | Audit a list and export JSON report |
| 🔐 Secure Login | SHA-256 hashed auth + constant-time compare |
| 💡 Generator | Cryptographically secure password suggestion |
| 📈 Strength Bar | Visual score bar with color indicators |
| 🖥️ Full CLI | No interactive mode required |

## Installation

```bash
git clone https://github.com/Ayham-Megdadi/ai_password_auditor.git
cd ai_password_auditor
python3 AI-Password-Auditor.py
```

> Zero external dependencies — pure Python stdlib.

## Usage

```bash
# Interactive mode (with login)
python3 AI-Password-Auditor.py

# Audit a single password
python3 AI-Password-Auditor.py audit "MyP@ssw0rd!" -u ayham -b 2004

# Batch audit from file
python3 AI-Password-Auditor.py batch passwords.txt --json

# Generate a strong password
python3 AI-Password-Auditor.py generate

## Example Output
Password  : admin

Strength  : Weak

Score     : 0/8  ░░░░░░░░░░░░░░░░░░░░

Entropy   : 23.5 bits
⚠  Too short (minimum 8 characters)

⚠  Found in known breach lists!
✦  Use at least 12–16 characters

✦  Add symbols and digits

## ⚠️ Disclaimer

This tool is intended **strictly for educational and ethical use**.  
Do not use it to audit passwords you do not own or have explicit permission to test.
```

## Example Output
