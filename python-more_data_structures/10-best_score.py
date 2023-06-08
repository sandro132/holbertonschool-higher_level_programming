#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    biggers = max(a_dictionary)
    return biggers