import os
import sys
import pickle


def get_file_size(file_path):
    return os.path.getsize(file_path)


def get_file_name_length(file_path):
    return len(os.path.basename(file_path))


def count_files_and_folders(path, max_count=sys.maxsize, serialized_results=None):
    try:
        if serialized_results is None:
            serialized_results = set()

        file_count = 0
        folder_count = 0
        largest_file = ("", 0)
        smallest_file = ("", sys.maxsize)
        longest_name = ("", 0)
        shortest_name = ("", sys.maxsize)

        for root, dirs, files in os.walk(path):
            for file in files:
                file_path = os.path.join(root, file)
                if file_path in serialized_results:
                    continue

                file_count += 1

                file_size = get_file_size(file_path)
                if file_size > largest_file[1]:
                    largest_file = (file_path, file_size)
                if file_size < smallest_file[1]:
                    smallest_file = (file_path, file_size)

                name_length = get_file_name_length(file_path)
                if name_length > longest_name[1]:
                    longest_name = (file_path, name_length)
                if name_length < shortest_name[1]:
                    shortest_name = (file_path, name_length)

                if file_count >= max_count:
                    print("Достигнуто максимальное количество файлов.")
                    return folder_count, file_count, largest_file, smallest_file, longest_name, shortest_name

            for folder in dirs:
                folder_count += 1

            serialized_results.add(file_path)

        return folder_count, file_count, largest_file, smallest_file, longest_name, shortest_name

    except KeyboardInterrupt:
        with open("serialized_results.pkl", "wb") as file:
            pickle.dump(serialized_results, file)
        print("Результаты сохранены. Перезапустите скрипт для продолжения.")
        sys.exit(0)


if __name__ == "__main__":
    path_to_check = input("Введите путь для проверки (или оставьте пустым для всей системы): ")
    max_file_count = int(input("Введите максимальное количество файлов для подсчета: "))

    if path_to_check == "":
        path_to_check = "/Users/" if sys.platform != "win32" else "C:\\"

    results = count_files_and_folders(path_to_check, max_count=max_file_count)
    print("Количество папок:", results[0])
    print("Количество файлов:", results[1])
    print("Самый большой файл:", results[2])
