def scan_files(files):
    files_info = []
    for filename in files:
        with open(filename, "r", encoding="utf-8") as file:
            files_info.append(
                {
                    'filename': filename,
                    'rows_number': len(file.read().split('\n'))
                }
            )
    return files_info


def sort_files(files):
    return sorted(files, key=lambda x: x['rows_number'])


def write_files(files):
    with open("result.txt", "w", encoding="utf8") as input_file:
        for file_info in files:
            # file_info = {'filename': '1.txt', 'rows_number': 8}
            with open(file_info['filename'], "r", encoding="utf8") as file:
                input_file.write(
                    file_info['filename'] + '\n' + str(file_info['rows_number']) + '\n' + file.read() + '\n'
                )


# Запись информации о файлах в список
files_list = scan_files(['1.txt', '2.txt', '3.txt'])
print(files_list)
# Сортировка файлов по числу строк
sorted_files = sort_files(files_list)
print(sorted_files)

# Запись файлов в один
write_files(sorted_files)


