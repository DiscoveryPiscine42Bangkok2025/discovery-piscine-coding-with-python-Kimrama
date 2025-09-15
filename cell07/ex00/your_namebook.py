#!/usr/bin/env python3

def array_of_names(name_dict: dict) -> list:
    return [f"{first.capitalize()} {last.capitalize()}" for first, last in name_dict.items()]

persons = {
    "jean": "valjean",
    "grace": "hopper",
    "xavier": "niel",
    "fifi": "brindacier"
}
print(array_of_names(persons))