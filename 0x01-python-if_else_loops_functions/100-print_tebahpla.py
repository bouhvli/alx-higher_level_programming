#!/usr/bin/python3
count = 1
for i in range(-122, -96):
    if count % 2 == 0:
        print(f"{chr(i*(-1)-32)}", end="")
        count += 1
        continue
    print(f"{chr(i*(-1))}", end="")
    count += 1
