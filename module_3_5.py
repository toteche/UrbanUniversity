def get_multiplied_digits(number):

    if number < 10:
        return number
    str_number = str(number)
    first = int(str_number[0])

    return first * get_multiplied_digits(int(str_number[1:]))



result = get_multiplied_digits(40203)

print(result)

