#!/usr/bin/python3
def roman_to_int(roman_string):
    dict = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    listint = [0] * len(roman_string)
    idx = 0
    for i in roman_string:
        for key, value in dict.items():
            if i == key:
                listint[idx] = value
        idx += 1
    som = 0
    prev = 0
    for idx in range(len(listint)):
        som += listint[idx]
        if idx != 0:
            if prev < listint[idx]:
                som -= listint[idx] + prev
                prev = listint[idx] - prev
                som += prev
        prev = listint[idx]
    return som
