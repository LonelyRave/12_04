def to_dict(lst):
    return {elem: elem for elem in lst}


if __name__ == '__main__':
    lst = ["apple", "banana", "cherry"]
    print(to_dict(lst))
