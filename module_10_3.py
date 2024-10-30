import random
import time
from threading import Lock, Thread

class Bank:
	def __init__(self):
		self.balance = 0
		self.lock = Lock()

	def deposit(self):
		for _ in range(100):
			amount = random.randint(50,500)
			self.balance += amount
			print(f'Пополнение: {amount}. Баланс: {self.balance}')
			if self.balance >= 500 and self.lock.locked():
				self.lock.release()
			time.sleep(0.001)

	def take(self):
		for _ in range(100):
			amount = random.randint(50,500)
			print(f'Запрос на {amount}')
			if amount <= self.balance:
				self.balance -= amount
				print(f'Снятие: {amount}. Баланс: {self.balance}')
			else:
				print("Запрос отклонен, недостаточно средств")
				self.lock.acquire()
			time.sleep(0.001)

bank = Bank()

deposit_thread = Thread(target=bank.deposit)
take_thread = Thread(target=bank.take)

deposit_thread.start()
take_thread.start()

deposit_thread.join()
take_thread.join()

print(f"Итоговый баланс: {bank.balance}")