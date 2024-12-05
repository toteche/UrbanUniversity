class Runner:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed

class Tournament:
    def __init__(self, distance, *runners):
        self.distance = distance
        self.runners = list(runners)

    def start(self):
        """Сортируем бегунов по скорости (от большей к меньшей)"""
        sorted_runners = sorted(self.runners, key=lambda x: x.speed, reverse=True)

        """Рассчитываем время прохождения дистанции для каждого бегуна"""
        results = {}
        for i, runner in enumerate(sorted_runners, 1):
            """Время = дистанция/скорость"""
            time = self.distance / runner.speed
            results[i] = runner

        """Возвращаем словарь, отсортированный по времени"""
        return results