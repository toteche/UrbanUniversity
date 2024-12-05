import unittest
from runner_improved import Runner, Tournament

class TournamentCorrectnessTest(unittest.TestCase):
    def test_time_calculation(self):
        """Проверка корректности рассчета времени"""
        usen = Runner('Усейн', 10)
        andrey = Runner('Андрей', 9)
        nick = Runner('Ник', 3)

        tournament = Tournament(90, usen, andrey, nick)
        result = tournament.start()

        """Проверка, что время пропорционально дистанции и обратно пропорционально скорости"""
        self.assertAlmostEqual(90/usen.speed, 90/result[1].speed, places=7)
        self.assertAlmostEqual(90/nick.speed, 90/result[3].speed, places=7)

    def test_order_consistency(self):
        """Проверка постоянности результатов"""
        runners = [
            Runner('Усейн', 10),
            Runner('Андрей', 9),
            Runner('Ник', 3)
        ]

        tournament = Tournament(90, *runners)
        result = tournament.start()

        """Проверка, что время Ника всегда максимальное"""
        self.assertTrue(result[max(result.keys())].name == 'Ник')

if __name__ == '__main__':
    unittest.main()