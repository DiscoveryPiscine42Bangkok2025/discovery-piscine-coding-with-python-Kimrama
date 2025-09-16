#!/usr/bin/env python3
inp1 = input("Give me the first number: ")
inp2 = input("Give me the second number: ")

try:
    num1 = float(inp1)
    num2 = float(inp2)
except ValueError:
    print("Error: invalid input")
    exit(1)

print("Thank you!")
print(f"{num1} + {num2} = {num1 + num2}")
print(f"{num1} - {num2} = {num1 - num2}")
if num2 == 0:
    print("Division by 0 is not allowed.")
else:
    print(f"{num1} / {num2} = {num1 / num2}")
print(f"{num1} * {num2} = {num1 * num2}")