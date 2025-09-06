def shift_text(text: str, k: int) -> str:
    k = k % 26  # normalize shift
    out = []
    for ch in text:
        if 'a' <= ch <= 'z':
            base = ord('a')
            out.append(chr(base + (ord(ch) - base + k) % 26))
        elif 'A' <= ch <= 'Z':
            base = ord('A')
            out.append(chr(base + (ord(ch) - base + k) % 26))
        else:
            out.append(ch)
    return ''.join(out)

def encrypt(text: str, k: int) -> str:
    return shift_text(text, k)

def decrypt(text: str, k: int) -> str:
    return shift_text(text, -k)

if __name__ == "__main__":
    mode = input("Choose mode - (E)ncrypt or (D)ecrypt: ").strip().lower()
    try:
        k = int(input("Enter shift value (integer): ").strip())
    except ValueError:
        print("Shift must be an integer.")
        raise SystemExit(1)
    message = input("Enter your message: ")

    if mode in ("e", "encrypt"):
        print("Encrypted:", encrypt(message, k))
    elif mode in ("d", "decrypt"):
        print("Decrypted:", decrypt(message, k))
    else:
        print("Invalid mode. Use E or D.")
