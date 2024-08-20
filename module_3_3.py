def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params()
print_params(b = 25)
print_params(c = [1,2,3])

values_list = [50, 'Иванов', True]
values_dict = {'a': 150, 'b': 'Петров', 'c': False}

values_list_2 = [54.32, 'Проверка связи']

print_params(*values_list)
print_params(**values_dict)
print_params(*values_list_2, 42)
