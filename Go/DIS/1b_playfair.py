
def matrix(k):
    s = ''.join(dict.fromkeys(k.upper().replace('J','I')+'ABCDEFGHIKLMNOPQRSTUVWXYZ'))
    return [s[i:i+5] for i in range(0,25,5)]

def playfair(msg,m,mode):
    msg=msg.upper().replace('J','I').replace(' ','')
    if mode==1:
        out,i='',0
        while i<len(msg):
            out+=msg[i]
            if i+1==len(msg): out+='X'; i+=1
            elif msg[i]==msg[i+1]: out+='X'; i+=1
            else: out+=msg[i+1]; i+=2
        msg=out
    out=''
    for a,b in zip(msg[::2],msg[1::2]):
        r,c=next((r,row.index(a)) for r,row in enumerate(m) if a in row)
        s,d=next((r,row.index(b)) for r,row in enumerate(m) if b in row)
        if r==s: out+=m[r][(c+mode)%5]+m[s][(d+mode)%5]
        elif c==d: out+=m[(r+mode)%5][c]+m[(s+mode)%5][d]
        else: out+=m[r][d]+m[s][c]
    return out

k=input("Enter keyword: ")
msg=input("Enter message: ")
m=matrix(k)
print("Playfair Matrix:")
print('\n'.join(' '.join(r) for r in m))
e=playfair(msg,m,1)
print("Encrypted:",e)
print("Decrypted:",playfair(e,m,-1))
