#  Write a Python function to sum all the numbers in a list.


def sum_add(numbers):
    total = 0
    for x in numbers:
        total += x
    return total
print(sum_add((8, 2, 3, 0, 7)))