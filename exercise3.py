num = int(input("Enter a number: "))
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = []

for v in a:
    if v < num:
        b.append(v)

for v in b:
    print(v)
