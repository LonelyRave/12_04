def change_list(lst):
    if len(lst) >= 2:
        lst[0], lst[-1] = lst[-1], lst[0]


if __name__ == '__main__':
    lst = [1, 2, 3, 4, 5]
    print("Before:", lst)
    change_list(lst)
    print("After:", lst)
