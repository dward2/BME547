import math


def do_math(in_list, item):
    x = in_list[item]
    y = in_list[item + 1]
    add = x + y
    subtract = x - y
    multi = x * y
    divi = x / y
    return [add, subtract, multi, divi]


def do_adv_math(in_list, item):
    x = in_list[item]
    y = in_list[item + 1]
    if x > 10:
        y = y * -1
    a = x * y
    b = math.sqrt(a)
    return b


def main():
    result_db = []
    my_list = [5, 45, 2, -2]
    for i in range(len(my_list)-1):
        result = do_adv_math(my_list, i)
        result_db.append(result)
    print(result_db)


if __name__ == "__main__":
    main()


