num = int(input("Enter a number to check: "))
check = int(input("Enter a number to divide by: "))
result = num % check

if result == 0 and (num % 4) == 0:
    print(f'{check} divides into {num} and is a multiple of 4')
elif result == 0:
    print(f'{check} divides into {num}, but not a multiple of 4')
else:
    print(f'{check} does not divide into {num}')
# elif num % 4 == 0:
#     print("This number is even and a multiple of 4")
# elif num % 2 == 0:
#     print("This number is even")
# else:
#     print("This number is odd")
