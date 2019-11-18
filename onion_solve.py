import base64

with open('onionlayerencoding.txt', mode='r') as f:
    s = f.read()
f.close()

for i in range(32):
    try:
        s = base64.b16decode(s)
    except:
        try:
            s = base64.b32decode(s)
        except:
            try:
                s = base64.b64decode(s)
            except:
                print('Decode Error...')
    # print(i)
print(s)
