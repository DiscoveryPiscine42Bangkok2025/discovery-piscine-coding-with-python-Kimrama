#!/usr/bin/env python3
def greetings(name=None):
    if name == None:
        name = "noble stranger"
    elif not isinstance(name, str):
        name = "Error! It was not a name."
    print(f"Hello, {name}.")

greetings('Alexandra')
greetings('Wil')
greetings()
greetings(42)