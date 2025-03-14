# Keylogger
A research-based keylogging tool for ethical cybersecurity testing and user activity tracking with full consent.

## ⚠ Disclaimer
This project is **strictly for educational and ethical purposes**. Unauthorized use for malicious intent is prohibited. Always obtain user consent before deploying.

## Features
- Logs keyboard inputs in a local file.
- Can be used for security monitoring and research.
- Does NOT collect sensitive data.

## Installation
```bash
pkg update && pkg upgrade -y && \
pkg install python -y && \
python --version 
pkg install git -y 
git clone https://github.com/Riju-Rahaman/Keylogger.git 
cd Keylogger 
pip install pynput 
termux-setup-storage
python keylogger.py
