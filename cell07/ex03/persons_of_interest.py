#!/usr/bin/env python3

# def key_to_sort(item):
#     return item[1]["date_of_birth"]

def famous_births(dict_of_dicts: dict) -> None:
    sorted_dob = dict(sorted(dict_of_dicts.items(), key=lambda item: item[1]["date_of_birth"]))
    for _, value in sorted_dob.items():
        print(f"{value['name']} is a great scientist born in {value['date_of_birth']}.")

women_scientists = {
    "ada": { "name": "Ada Lovelace", "date_of_birth": "1815" },
    "cecilia": { "name": "Cecila Payne", "date_of_birth": "1900" },
    "lise": { "name": "Lise Meitner", "date_of_birth": "1878" },
    "grace": { "name": "Grace Hopper", "date_of_birth": "1906" }
}
famous_births(women_scientists)