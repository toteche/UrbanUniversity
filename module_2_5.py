def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        row = []
        for j in range(m):
            row.append(value)
        matrix.append(row)
    return matrix

n = int(input('Введите количество строк (n): '))
m = int(input('Введите количество столбцов (m): '))
value = input('Введите значение (value): ')

result = get_matrix(n, m, value)
print(result)