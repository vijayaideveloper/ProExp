import numpy as np

K = np.array([[1,2,1],[2,3,2],[2,2,1]])
I = np.array([[-1,0,1],[2,-1,0],[-2,2,-1]])

def process(text, key):
    text = text.upper().replace(" ", "")
    text += "X" * (-len(text) % 3)
    return ''.join(chr(int(n) + 65) for i in range(0, len(text), 3)
                   for n in np.dot(key, [ord(c)-65 for c in text[i:i+3]]) % 26)

p = input("Enter plain text: ").upper().replace(" ", "")
p += "X" * (-len(p) % 3)
e = process(p, K)
print("Padded Text:", p)
print("Encrypted:", e)
print("Decrypted:", process(e, I))