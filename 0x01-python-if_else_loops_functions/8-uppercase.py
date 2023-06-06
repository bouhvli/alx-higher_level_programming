#!/usr/bin/python3
def uppercase(str):
    sil = list(str)
    for i in range(0, len(str)):
        lower = ord(str[i])
        if lower in range(97, 122):
            sil[i] = chr(lower - 32)
        else:
            continue
    print("{}".format(''.join(sil)))
