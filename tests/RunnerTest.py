import unittest
from runner import Runner
from functools import wraps

def skip_if_frozen(message='Тесты в этом кесе заморожены'):
	def decorator(func):
		@wraps(func)
		def wrapper(self, *args, **kwargs):
			if hasattr(self, 'is_frozen') and self.is_frozen:
				self.skipTest(message)
			return func(self, *args, **kwargs)
		return wrapper
	return decorator


class RunnerTest(unittest.TestCase):
	is_frozen = False

	@skip_if_frozen()
	def test_walk(self):
		runner = Runner("Иван")
		for _ in range(10):
			runner.walk()

		self.assertEqual(runner.distance, 50)

	@skip_if_frozen()
	def test_run(self):
		runner = Runner("Олег")
		for _ in range(10):
			runner.run()

		self.assertEqual(runner.distance, 100)

	@skip_if_frozen()
	def test_challenge(self):
		runner1 = Runner("Алиса")
		runner2 = Runner("Сири")
		for _ in range(10):
			runner1.run()

		for _ in range(10):
			runner2.walk()

		self.assertNotEqual(runner1.distance, runner2.distance)

if __name__ == "__main__":
	unittest.main()