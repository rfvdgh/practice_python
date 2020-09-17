#! usr/bin/env python3

name = input("Greetings, Friend. Please enter your name: ") 
age = int(input("Please enter your age: "))

years_to_100 = 100 - age
year = 2020 + years_to_100

print(f'{name} will be 100 years old in {year}')
