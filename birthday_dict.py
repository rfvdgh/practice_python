#! usr/bin/env python3
# adding code here for git practice
import json


def add_person():
    person = str(input("Enter name of person you want to add: "))
    b_day = str(input("Enter birthday of person: "))
    # dict constructor with named variables
    entry = dict([(person,b_day)])
    with open("info.json", mode='rt') as f:
        file = json.load(f)

    file.update(entry)
    with open("info.json", mode='wt') as f:
        json.dump(file, f)


def main():

    with open("info.json", mode='rt') as f:
        info = json.load(f)

    print("Welcome to the brithday dictionary. We know birthdays of:\n")

    for name in info:
        print(name)

    choice = str(input("Who's birthday do you want to look up? "))

    for k in info:
        if choice == k:
            print(info[k])

if __name__ == '__main__':
    main()
