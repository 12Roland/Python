
#!/usr/bin/env python3
"""
Interactive Password Generator (Naturally)
Uses `secrets` for cryptographically secure random choices.
"""

import secrets
import string
import sys

try:
    import pyperclip  # optional, pip install pyperclip
    PYPERCLIP_AVAILABLE = True
except ImportError:
    PYPERCLIP_AVAILABLE = False

def generate_password(length=12, use_upper=True, use_digits=True, use_special=True):
    if length < 1:
        raise ValueError("Password length must be >= 1")

    alphabet = list(string.ascii_lowercase)
    if use_upper:
        alphabet += list(string.ascii_uppercase)
    if use_digits:
        alphabet += list(string.digits)
    if use_special:
        # a reasonable set of symbols; you can change this
        alphabet += list("!@#$%^&*()-_=+[]{};:,.<>/?")

    # Ensure at least one of each selected category is present
    password_chars = []
    password_chars.append(secrets.choice(string.ascii_lowercase))
    if use_upper:
        password_chars.append(secrets.choice(string.ascii_uppercase))
    if use_digits:
        password_chars.append(secrets.choice(string.digits))
    if use_special:
        password_chars.append(secrets.choice("!@#$%^&*()-_=+[]{};:,.<>/?"))

    # Fill the rest
    while len(password_chars) < length:
        password_chars.append(secrets.choice(alphabet))

    # Shuffle securely
    secrets.SystemRandom().shuffle(password_chars)
    return ''.join(password_chars[:length])


def main():
    print("=== Secure Password Generator ===")
    try:
        length = int(input("Password length (e.g. 12): ").strip() or "12")
    except ValueError:
        print("Invalid length. Using default 12.")
        length = 12

    def ask_bool(prompt, default=True):
        ans = input(f"{prompt} [{'Y' if default else 'y'}/{'n' if default else 'N'}]: ").strip().lower()
        if ans == "":
            return default
        return ans[0] == "y"

    use_upper = ask_bool("Include UPPERCASE letters?", True)
    use_digits = ask_bool("Include digits?", True)
    use_special = ask_bool("Include special characters?", True)

    pwd = generate_password(length, use_upper, use_digits, use_special)
    print("\nGenerated password:\n", pwd)

    if PYPERCLIP_AVAILABLE:
        try:
            pyperclip.copy(pwd)
            print("(Copied to clipboard.)")
        except Exception:
            print("(Couldn't copy to clipboard.)")
    else:
        print("(Tip: install `pyperclip` to allow copying to clipboard: pip install pyperclip)")

    save = input("Save this password to a local file? (not recommended for sensitive passwords) [n/Y]: ").strip().lower()
    if save and save[0] == "y":
        filename = input("Filename (default: passwords.txt): ").strip() or "passwords.txt"
        note = input("Optional note (e.g. 'gmail account'): ").strip()
        with open(filename, "a", encoding="utf-8") as f:
            f.write(f"{pwd}\t{note}\n")
        print(f"Saved to {filename} (remember: storing plaintext passwords is insecure).")

if __name__ == "__main__":
    main()
