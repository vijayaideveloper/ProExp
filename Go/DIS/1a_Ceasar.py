def encrypt(s, k):
    return ''.join(chr((ord(c)-97+k)%26+97) if c.isalpha() else c for c in s.lower())

def decrypt(s, k):
    return encrypt(s, -k)

msg = input("Enter text: ")
enc = encrypt(msg, 3)
print("Encrypted:", enc)
print("Decrypted:", decrypt(enc, 3))