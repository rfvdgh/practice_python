#! usr/bin/env/ python

import sys

def get_divisors(num):
    divisors = []
    x = list(range(1,num + 1))
    
    for i in x:
        if (x[-1] % i) == 0:
            divisors.append(i)

    return divisors

def print_divisors(divisors):
    for i in divisors:
        print(i)

def main():
    print("Enter a number to retrieve known divisors")
    num = int(input("Enter your value: "))
    x = get_divisors(num)
    print_divisors(x)


if __name__ == '__main__':
    main()