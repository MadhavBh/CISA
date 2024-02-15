h = "add"
a = 23

res = ''.join(format(ord(i), '08b') for i in h)

print(bytes(res, 'utf-8'))

chunks = [res[i:i+8] for i in range(0, len(res), 8)]

string = ''.join(chr(int(chunk, 2)) for chunk in chunks)

print(string)
#01100001 01100100 01100100
