import time
from threading import Thread

class Knight(Thread):
	def __init__(self, name, power):
		super().__init__()
		self.name = name
		self.power = power
		self.enemies = 100

	def run(self):
		print(f'{self.name}, на нас напали!')
		days = 0

		while self.enemies > 0:
			self.enemies -= self.power
			days += 1
			time.sleep(1) # 1 секунда = 1 день
			print(f'{self.name} сражается {days}..., осталось {self.enemies} воинов.')

		print(f'{self.name} одержал победу спустя {days} дней!')

knight1 = Knight('Сэр Галахад', 25)
knight2 = Knight('Сэр Ланселот', 30)

knight1.start()
knight2.start()

knight1.join()
knight2.join()

print("Битвы завершены")