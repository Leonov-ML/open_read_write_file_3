import os

path = '.'
list = []

if "service_file.txt" in os.listdir(path):
    os.remove("service_file.txt")

# Функция получения списка файлов '.txt' в корневом каталоге.
for file in os.listdir(path):
    if file.endswith(".txt"):
        list.append(os.path.join(file))
if len(list) == 0:
    print('Нет файлов соответствующего расширения! Попробуйте снова.')
    exit()

temp = {}

for file in list:
    name = file
    with open(file, encoding='utf-8') as file:
        lines = file.readlines()
        temp[name] = (len(lines))

sorted_dict = {}
sorted_keys = sorted(temp, key=temp.get)

for w in sorted_keys:
    sorted_dict[w] = temp[w]

#print(sorted_dict)

service = open("service_file.txt", "w+", encoding='utf-8')
for i in sorted_dict:
    service.write(f'{i}\n')
    service.write(f'{sorted_dict[i]}\n')
    for num in range(sorted_dict[i]):
        service.write(f'Строка номер {num + 1} файла номер {i.strip(".txt")}\n')
print('Запись завершена, файл "service_file.txt" успешно создан.')
service.close()
