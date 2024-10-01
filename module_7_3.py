import re

class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = list(file_names)

    def get_all_words(self):
        all_words = {}

        for file_name in self.file_names:
            try:
                with open(file_name, 'r', encoding='utf-8') as file:
                    words_list = []
                    for line in file:
                        line = line.lower()
                        line = re.sub(r"[',.!?;:=-]", "", line)
                        words = line.split()
                        words_list.extend(words)
                    all_words[file_name] = words_list
            except FileNotFoundError:
                print(f'Файл {file_name} не найден.')
        return all_words

    def find(self, word):
        all_words = self.get_all_words()
        word = word.lower()
        word_positions = {}

        for file_name, words in all_words.items():
            try:
                position = words.index(word) + 1
                word_positions[file_name] = position
            except ValueError:
                word_positions[file_name] = None
        return word_positions

    def count(self, word):
        all_words = self.get_all_words()
        word = word.lower()
        word_counts = {}

        for file_name, words in all_words.items():
            count = words.count(word)
            word_counts[file_name] = count
        return word_counts



finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего