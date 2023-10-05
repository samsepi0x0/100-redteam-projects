def encrypt(message):
    new_message = ""

    for i in range(0, len(message)):
        ch = message[i]
        val = ord(ch)

        if val >= 65 and val <= 90:
            new_val = val + 13
            if new_val > 90:
                new_val = (new_val - 90) + 64
            val = new_val
        
        if val >= 97 and val <= 122:
            new_val = val + 13
            if new_val > 122:
                new_val = (new_val - 122) + 96
            val = new_val
        
        new_message += chr(val)
    return new_message

def decrypt(message):
    new_message = ""

    for i in range(0, len(message)):
        ch = message[i]
        val = ord(ch)

        if val >= 65 and val <= 90:
            new_val = val - 13
            if new_val < 65:
                new_val = 91 - (65 - new_val)
            val = new_val

        if val >= 97 and val <= 122:
            new_val = val - 13
            if new_val < 97:
                new_val = 123 - (97 - new_val)
            val = new_val

        new_message += chr(val)
    return new_message

def main():
    sentence = input(">> ")
    enc = encrypt(sentence)
    print(f"Encrypted: {enc}")

    dec = decrypt(enc)
    print(f"Decrypted: {dec}")

if __name__ == "__main__":
    main()