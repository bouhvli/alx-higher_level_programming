#!/usr/bin/python3
def remove_char_at(str, n):
    sil = list(str)
    for i in range(0, len(str)):
        if i == n:
            del sil[i]
    return ''.join(sil)
