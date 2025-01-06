import unittest
import logging

from Runner_12_4 import Runner

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    filename="runner_tests.log",
    filemode="w",
    encoding="utf-8",
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class RunnerTest(unittest.TestCase):
    def test_walk(self):
        try:
            # Для тестирования передаем отрицательную скорость
            runner = Runner("Иван", speed=-5)
            for _ in range(10):
                runner.walk()
            self.assertEqual(runner.distance, 50)
            logging.info('"test_walk" выполнен успешно')
        except ValueError as e:
            logging.warning("Неверная скорость для Runner: %s", e)

    def test_run(self):
        try:
            # Для тестирования передаем неверный тип в name
            runner = Runner(12345, speed=5)
            for _ in range(10):
                runner.run()
            self.assertEqual(runner.distance, 100)
            logging.info('"test_run" выполнен успешно')
        except TypeError as e:
            logging.warning("Неверный тип данных для обьекта Runner: %s", e)

    def test_challenge(self):
        runner1 = Runner("Алиса")
        runner2 = Runner("Сири")
        for _ in range(10):
            runner1.run()
        for _ in range(10):
            runner2.walk()
        self.assertNotEqual(runner1.distance, runner2.distance)
        logging.info('"test_challenge" выполнен успешно')