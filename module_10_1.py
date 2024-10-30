import time
from time import sleep
from threading import Thread

def write_words(word_count, file_name):
    with open(file_name, 'w') as file:
        for i in range(1, word_count + 1):
            word = f'Какое-то слово № {i}'
            file.write(word + "\n")
            # print(word)
            sleep(0.1)
    print(f'Завершилась запись в файл {file_name}')

write_words(10, "example1.txt")
write_words(30, "example2.txt")
write_words(200, "example3.txt")
write_words(100, "example4.txt")

def run_write_word_threads():
    start_time = time.time()

    threads = [
        Thread(target=write_words, args=(10, "example5.txt")),
        Thread(target=write_words, args=(30, "example6.txt")),
        Thread(target=write_words, args=(200, "example7.txt")),
        Thread(target=write_words, args=(100, "example8.txt"))
    ]

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    end_time = time.time()
    print(f'Работа потоков {end_time - start_time}')

run_write_word_threads()