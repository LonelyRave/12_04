from task1 import is_power_of_two
from task2 import square
from task3 import is_prime
from task4 import change_list
from task5 import to_dict
from task6 import sum_range

if __name__ == '__main__':
    n = int(input("Enter a number: "))
    if is_power_of_two(n):
        print("YES")
    else:
        print("NO")

    side = int(input("Enter the side of the square: "))
    print(square(side))

    n = int(input("Enter a number between 2 and 1000: "))
    if is_prime(n):
        print("PRIME")
    else:
        print("NOT PRIME")

    lst = [1, 2, 3, 4, 5]
    print("Before:", lst)
    change_list(lst)
    print("After:", lst)

    lst = ["apple", "banana", "cherry"]
    print(to_dict(lst))

start = int(input("Enter the start number: "))
end = int(input("Enter the end number: "))
if start > end:
    start, end = end, start
print(sum_range(start, end))
