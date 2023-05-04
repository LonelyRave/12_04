def sum_range(start, end):
    if start > end:
        start, end = end, start
    return sum(range(start, end + 1))


if __name__ == '__main__':
    start = int(input("Enter the start value: "))
    end = int(input("Enter the end value: "))
    print(sum_range(start, end))