class House:
    houses_history = []

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Название - {self.name}, количество этажей {self.number_of_floors}'

    def __eq__(self, other):
        if isinstance(other, int) or isinstance(other, House):
            return self.number_of_floors == other.number_of_floors
        else:
            raise ValueError('Значение должно быть положительным целым числом')

    def __lt__(self, other):
        if isinstance(other, int) or isinstance(other, House):
            return self.number_of_floors < other.number_of_floors
        else:
            raise ValueError('Значение должно быть положительным целым числом')

    def __le__(self, other):
        if isinstance(other, int) or isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors
        else:
            raise ValueError('Значение должно быть положительным целым числом')

    def __gt__(self, other):
        if isinstance(other, int) or isinstance(other, House):
            return self.number_of_floors > other.number_of_floors
        else:
            raise ValueError('Значение должно быть положительным целым числом')

    def __ge__(self, other):
        if isinstance(other, int) or isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors
        else:
            raise ValueError('Значение должно быть положительным целым числом')

    def __ne__(self, other):
        if isinstance(other, int) or isinstance(other, House):
            return self.number_of_floors != other.number_of_floors
        else:
            raise ValueError('Значение должно быть положительным целым числом')

    def __add__(self, value):
        if isinstance(value, int) and value > 0:
            self.number_of_floors += value
        else:
            raise ValueError('Значение должно быть положительным целым числом')
        return self

    def __radd__(self, value):
        return self.__add__(value)

    def __iadd__(self, value):
        return self.__add__(value)

    def go_to(self, new_floor):
        if 1 <= new_floor <= self.number_of_floors:
            for i in range(1, new_floor +1):
                print(i)
            else:
                print("Такого этажа не существует!")

    def __new__(cls, *args, **kwargs):
        house_name = args[0]
        cls.houses_history.append(house_name)
        return super().__new__(cls)

    def __del__(self):
        print(f'{self.name} снесен, но останется в истории')

h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)


