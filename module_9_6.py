def all_variants(text):

    # Получаем длину строки
    n = len(text)

    # Создаем битовые маски для всех возможных подмножеств
    for mask in range(2 ** n):
        variant = ""
        for i in range(n):
            # Если бит на месте i установлен, добавляем соответствующий символ в вариант
            if mask & (1 << i):
                variant += text[i]
        yield variant


# Пример использования
a = all_variants("abc")
for i in a:
    print(i)