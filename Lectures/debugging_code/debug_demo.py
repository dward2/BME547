def do_math(in_list, item):
    x = in_list[item]
    y = in_list[item + 1]
    add = x + y
    subtract = x - y
    multi = x * y
    divi = x / y
    return [add, subtract, multi, divi]


def main():
    result_db = []
    my_list = [5, 10, 0, -2]
    for i in range(len(my_list)):
        result = do_math(my_list, i)
        result_db.append(result)


if __name__ == "__main__":
    main()


