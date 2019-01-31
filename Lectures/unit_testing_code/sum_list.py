# sum_list.py


def sum_list(input_list):
    # output = sum(input_list)
    output = 0
    for number in input_list:
        if type(number) == str:
            actual_number = float(number)
        else:
            actual_number = number
        output += actual_number

    return output


def is_in_shopping_list(item, shopping_list):
    cleaned_item = item.strip()
    if cleaned_item in shopping_list:
        return True
    else:
        return False


