#!/usr/bin/python3
for i in range(10):
    for x in range(i+1, 10):
        print(f"{i :d}{x :d}", end='')
        if (i == 8 and x == 9):
            break
        print(f", ", end='')
