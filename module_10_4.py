from threading import Thread
from queue import Queue
import time
import random

class Table:
    def __init__(self, number):
        self.number = number
        self.guest = None

class Guest(Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        #Гость находится за столом от 3 до 10 секунд
        time.sleep(random.uniform(3, 10))

class Cafe:
    def __init__(self, *tables):
        self.queue = Queue()
        self.tables = tables

    def guest_arrival(self, *guests):
        for guest in guests:
            # Поиск свободного стола
            free_table = None
            for table in self.tables:
                if table.guest is None:
                    free_table = table
                    break

            if free_table:
                # Если есть свободный стол - сажаем гостя
                free_table.guest = guest
                guest.start()
                print(f'{guest.name} размещен(-а) за стол номер {free_table.number}')
            else:
                # Если нет свободных столов - ставим гостя в очередь
                self.queue.put(guest)
                print(f'{guest.name} пока что в очереди')

    def discuss_guests(self):
        while not self.queue.empty() or any(table.guest is not None for table in self.tables):
            for table in self.tables:
                if table.guest is not None:
                    # Проверяем, закончил ли гость есть
                    if not table.guest.is_alive():
                        print(f'{table.guest.name} поел(-а) и ушел(ушла)')
                        print(f'Стол номер {table.number} освободился')
                        table.guest = None

                        # Если в очереди гости, садим следущего
                        if not self.queue.empty():
                            next_guest = self.queue.get()
                            table.guest = next_guest
                            print(f'{next_guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}')

            # Небольшая пауза перед следующей проверкой
            time.sleep(0.1)

# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()
