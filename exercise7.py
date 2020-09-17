a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

b = [v for v in a if v % 2 == 0]
print(b)

# extra not included in exercise, x and y do not exist outside of this comprehension
c = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]
print(c)
