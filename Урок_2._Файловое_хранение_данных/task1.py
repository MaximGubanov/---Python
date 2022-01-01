import csv

def get_data():
    files = ['info_1.txt', 'info_2.txt', 'info_3.txt']
    main_data = [['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы']]
    for file in files:
        os_prod_list = []
        os_name_list = []
        os_code_list = []
        os_type_list = []
        with open(file, encoding="windows-1251") as f:
            data = f.read().split('\n')
            for line in data:
                s = line.split(':')
                if 'Изготовитель системы' in s[0]:
                    os_prod_list.append(s[1].strip())
                if 'Название ОС' in s[0]:
                    os_name_list.append(s[1].strip())
                if 'Код продукта' in s[0]:
                    os_code_list.append(s[1].strip())
                if 'Тип системы' in s[0]:
                    os_type_list.append(s[1].strip())
            main_data.append(
                [
                    os_prod_list[:1][0],
                    os_name_list[:1][0],
                    os_code_list[:1][0],
                    os_type_list[:1][0],
                ]
            )
    return main_data


def write_to_csv(file_name):
    with open(file_name, 'w') as file_csv:
        csv_writer = csv.writer(file_csv)
        print(get_data())
        for row in get_data():
            csv_writer.writerow(row)

write_to_csv('new_test_csv')