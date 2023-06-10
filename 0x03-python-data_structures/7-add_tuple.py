#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    va1 = tuple_a[0] if len(tuple_a) >= 1 else 0
    va2 = tuple_a[1] if len(tuple_a) >= 2 else 0
    vb1 = tuple_b[0] if len(tuple_b) >= 1 else 0
    vb2 = tuple_b[1] if len(tuple_b) >= 2 else 0
    som1 = va1 + vb1
    som2 = va2 + vb2
    return tuple((som1, som2))
