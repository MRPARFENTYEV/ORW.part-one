d = open("data.txt", "r", encoding="utf-8")
print(d)

cook_book = {}
s = d.readline()
# print(s)
while s != "":
    name = s[:-1]  # name = название блюда
    print(name)

    all_ing = []  # all_ing = ингридиенты блюда
    print(all_ing)

    a = int(d.readline()[:-1])  # a = кол-во ингридиентов
    print(a)
    for i in range(a):
        x = d.readline()[:-1]
        # print(x)
        ing = x.split("|")  # список описания ингридиентов
        info = {'ingredient_name': ing[0].strip(), 'quantity': int(ing[1].strip()), 'measure': ing[2].strip()}
        all_ing.append(info)
    cook_book[name] = all_ing

    s = d.readline()
    if s == "":
        break
    s = d.readline()
print(cook_book)


def get_shop_list_by_dishes(dishes, person_count):
    empty_dict = {}
    for dish in dishes:
        ingr = cook_book[dish]  # делает тоже самое что и 31 строчка
        for ing in ingr:
            name = ing['ingredient_name']
            quantity = ing['quantity']
            measure = ing['measure']
            if name in empty_dict:
                empty_dict[name]["quantity"]+= person_count*quantity
            else:
                empty_dict[name] = {"quantity":quantity*person_count,'measure':measure }
    return empty_dict


print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет', 'Фахитос'], 7))

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


