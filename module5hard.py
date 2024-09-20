import hashlib
from typing import List
from time import sleep

class User:
    """
    Класс пользователя, содержащий атрибуты: nickname(имя пользователя, строка), password(в хэшированном виде, число), age(возраст, число)
    """

    def __init__(self, nickname: str, password: str, age: int):
        self.nickname = nickname
        self.password = self.hash_password(password)
        self.age = age

    def hash_password(self, password: str) -> int:
        """ Хешируем пароль и возвращаем число"""
        return int(hashlib.sha256(password.encode()).hexdigest(), 16)

class Video:
    """
    Класс Video, содержащий атрибуты:  title(заголовок, строка), duration(продолжительность, секунды), time_now(секунда остановки (изначально 0)), adult_mode(ограничение по возрасту, bool (False по умолчанию))
    """

    def __init__(self, title: str, duration: int, adult_mode: bool = False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode

class UrTube:

    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname: str, password: str):
        for user in self.users:
            if user.nickname == nickname:
                self.current_user = user
                print(f'Пользователь {user} вошел в систему.')
                return
        print('Неверный логин или пароль.')

    def register(self, nickname: str, password: str, age: int):
        for user in self.users:
            if user.nickname == nickname:
                print(f"Пользователь {nickname} уже существует.")
                return
        new_user = User(nickname, password, age)
        self.users.append(new_user)
        self.current_user = new_user
        print(f"Пользователь {nickname} успешно зарегистрирован и вошёл в систему.")


    def log_out(self):
        if self.current_user:
            print(f'Пользователь {self.current_user.nickname} вышел из системы')
            self.current_user = None
        else:
            print('Чтобы начать просмотр, войдите в систему.')

    def add(self, *videos: Video):
        for video in videos:
            if any(existing_video.title == video.title for existing_video in self.videos):
                print(f'Видео с названием "{video.title}" уже существует.')
            else:
                self.videos.append(video)
                print(f'Видео "{video.title}" успешно добавлено')

    def get_videos(self, search_term: str) -> List[str]:
        search_term_lower = search_term.lower()
        return [video.title for video in self.videos if search_term_lower in video.title.lower()]

    def watch_video(self, title: str):
        if not self.current_user:
            print(f'Войдите в аккаунт, чтобы смотреть видео')
            return

        for video in self.videos:
            if video.title == title:
                if video.adult_mode and self.current_user.age < 18:
                    print('Вам еще нет 18. Просмотр данного видео у вас в будущем.')
                    return

                print(f'Начинаем просмотр видео {video.title}')
                for second in range(video.time_now, video.duration):
                    print(f'Секунда {second +1}')
                    sleep(1)
                video.time_now = 0
                print("Видео закончилось.")
                return
        print("Видео не найдено.")

ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# # Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))
#
# # Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')
#
# # Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')