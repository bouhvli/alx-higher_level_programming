#!/usr/bin/python3
def best_score(a_dictionary):
    max_score = 0
    if a_dictionary is None:
        return (None)
    for key, value in a_dictionary.items():
        if max_score < value:
            max_score = value
            max_score_key = key
        else:
            continue
    if max_score == 0:
        return (None)
    return (max_score_key)
