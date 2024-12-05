import unittest
from runner2 import Runner, Tournament


class TournamentTest(unittest.TestCase):
    all_results = {}

    @classmethod
    def setUpClass(cls):
        """Создание словаря для хранения результатов тестов"""
        cls.all_results = {}

    def setUp(self):
        """Создание объектов бегунов перед каждым тестом"""
        self.usen = Runner('Усэйн', 10)
        self.andrey = Runner('Андрей', 9)
        self.nick = Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        """Вывод результатов тестов"""
        print("\nРезультаты тестов:")
        for key, value in sorted(cls.all_results.items()):
            """Форматируем значение, заменяя обьекты Runner их именами"""
            formatted_value = {k: v.name if isinstance(v, Runner) else v for k, v in value.items()}
            print(f"{key}: {formatted_value}")

    def test_usen_and_nick(self):
        """Тест забега Усэйн и Ник"""
        tournament = Tournament(90, self.usen, self.nick)
        result = tournament.start()
        self.all_results[1] = result
        self.assertTrue(list(result.values())[-1] == 'Ник')

    def test_andrey_and_nick(self):
        """Тест забега Андрей и Ник"""
        tournament = Tournament(90, self.andrey, self.nick)
        result = tournament.start()
        self.all_results[2] = result
        self.assertTrue(list(result.values())[-1] == 'Ник')

    def test_usen_andrey_and_nick(self):
        """Тест забега Усэйн, Андрей и Ник"""
        tournament = Tournament(90, self.usen, self.andrey, self.nick)
        result = tournament.start()
        self.all_results[3] = result
        self.assertTrue(list(result.values())[-1] == 'Ник')


if __name__ == '__main__':
    unittest.main()