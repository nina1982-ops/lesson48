# Алгоритм работы кода:
# Импорты необходимых модулей и функций
# Объявление функции write_words
# Взятие текущего времени
# Запуск функций с аргументами из задачи
# Взятие текущего времени
# Вывод разницы начала и конца работы функций
# Взятие текущего времени
# Создание и запуск потоков с аргументами из задачи
# Взятие текущего времени
# Вывод разницы начала и конца работы потоков


from time import sleep
from datetime import datetime
from threading import Thread

def write_words(word_count, file_name):

    # word_count - количество записываемых слов,
    # file_name - название файла, куда будут записываться слова

    with open(file_name, 'w', encoding='utf-8') as f:

        for i in range(1, word_count + 1):
            word = f"Какое-то слово № {i}\n"
            f.write(word)
            sleep(0.1)
    print(f'Завершилась запись в файл {file_name}')

start_time = datetime.now()

write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')

end_time = datetime.now()
execution_time = end_time - start_time

print(f'Работа потоков {execution_time}')

start_time = datetime.now()

threads = []
threads.append(Thread(target=write_words, args=(10, "example5.txt")))
threads.append(Thread(target=write_words, args=(30, "example6.txt")))
threads.append(Thread(target=write_words, args=(200, "example7.txt")))
threads.append(Thread(target=write_words, args=(100, "example8.txt")))

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

end_time = datetime.now()
execution_time = end_time - start_time
print(f'Работа потоков {execution_time}')