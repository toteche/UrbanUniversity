def personal_sum(numbers):
    result = 0
    incorrect_data = 0
    for item in numbers:
        try:
            result += item
        except TypeError:
            incorrect_data += 1
    return result, incorrect_data

def calculate_average(numbers):
    try:
        if not isinstance(numbers, (list, tuple, set)):
            for item in numbers:
                if not isinstance(item, (int, float)):
                    print(f'Некорректный тип данных для подсчёта суммы -{item}')
            return None

        sum_result, incorrect_count = personal_sum(numbers)
        if incorrect_count > 0:
            for item in numbers:
                if isinstance(item, str):
                    print(f'Некорректный тип данных для подсчёта суммы -{item}')
                # return None
        print(f"Обнаружено {incorrect_count} некорректных данных")

        if len(numbers) == 0:
            return 0
        return sum_result / (len(numbers) - incorrect_count)
    except ZeroDivisionError:
        return 0
    except TypeError as e:
        print(f'Некорректный тип данных в numbers:{e}')
        return None

print(f'Результат 1: {calculate_average("1, 2, 3")}') # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}') # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}') # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}') # Всё должно работать