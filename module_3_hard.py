def calculate_structure_sum(data_structure):
    total_sum = 0
    total_string_lengths = 0

    def calculate(data):
        nonlocal total_sum, total_string_lengths
        if isinstance(data, (int, float)):
            total_sum += data
            print(f'\033[94mДобавили число: {data}, текущая сумма: {total_sum}')
        elif isinstance(data, str):
            total_string_lengths += len(data)
            print(f'\033[93mДобавили длину строки: {data}, текущая сумма: {total_string_lengths}')
        elif isinstance(data, (list, tuple, set)):
            for sub_item in data:
                calculate(sub_item)
        elif isinstance(data, dict):
            for key, value in data.items():
                if isinstance(key, str):
                    total_string_lengths += len(key)
                    print(f'\033[93mДобавили длину ключа (строка): {len(key)}, текущая сумма: {total_string_lengths}')
                elif isinstance(key, int):
                    total_sum += key
                    print(f'\033[94mДобавили ключ (число): {key}, текущая сумма: {total_sum}')

                if isinstance(value, str):
                    total_string_lengths += len(value)
                    print(f'\033[93mДобавили длину значения (строка): {len(value)}, текущая сумма: {total_string_lengths}')
                elif isinstance(value, int):
                    total_sum += value
                    print(f'\033[94mДобавили значение (число): {value}, текущая сумма: {total_sum}')



    calculate(data_structure)
    print('Total Sum:', total_sum)
    print(f'\033[93mTotal String length:, {total_string_lengths}')
    return total_sum + total_string_lengths

data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(f'\033[96mИтоговое число: {result}')

