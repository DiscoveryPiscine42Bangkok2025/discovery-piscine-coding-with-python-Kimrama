#!/usr/bin/env python3

class_3B = {
    "marine": 18,
    "jean": 15,
    "coline": 8,
    "luc": 9
}
class_3C = {
    "quentin": 17,
    "julie": 15,
    "marc": 8,
    "stephanie": 13
}

def average(class_dict: dict) -> float:
    if len(class_dict) == 0:
        return 0.0
    return sum(class_dict.values()) / len(class_dict)

print(f"Average for class 3B: {average(class_3B)}.")
print(f"Average for class 3C: {average(class_3C)}.")