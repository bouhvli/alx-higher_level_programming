#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    va1, va2 = tuple_a + (0,) * (2 - len(tuple_a))
    vb1, vb2 = tuple_b + (0,) * (2 - len(tuple_b))
    som1 = va1 + vb1
    som2 = va2 + vb2
    new_tuple = (som1, som2)
    return new_tuple
