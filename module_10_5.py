import time
import multiprocessing

def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        while True:
            line = file.readline()
            if not line:
                break
            all_data.append(line.strip())  # Добавляем строку в список, удаляя лишние пробелы
    # Не требуется возвращение all_data, ведь пример не требует этого.
if __name__ == '__main__':
    filenames = [f'file {number}.txt' for number in range(1, 5)]  # Пример имен файлов

    # Линейный вызов
    start_time = time.time()
    for filename in filenames:
        read_info(filename)
    linear_duration = time.time() - start_time
    print(f"{linear_duration:.6f} (линейный)")

    # Многопроцессный вызов
    start_time = time.time()
    with multiprocessing.Pool() as pool:
        pool.map(read_info, filenames)
    multiprocess_duration = time.time() - start_time
    print(f"{multiprocess_duration:.6f} (многопроцессный)")