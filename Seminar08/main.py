# Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt. Фамилия, имя, отчество,
# номер телефона - данные, которые должны находиться в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в текстовом файле
# 3. Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию человека)
# 4. Использование функций. Ваша программа не должна быть линейной


def read_file():
    with open(path_file, 'r', encoding='UTF-8') as f:
        for line in f:
            print(line.strip())


def write_file():
    with open(path_file, 'a', encoding='UTF-8') as f:
        f.writelines('\n' + input('Введите новую запись в формате "Фамилия Имя Отчество Телефон": '))
    print("Запись успешно добавлена в справочник")


def find_file():
    find_info = input('Введите значение поля, которое нужно найти: ')
    with open(path_file, 'r', encoding='UTF-8') as f:
        for line in f:
            if find_info.casefold() in line.casefold():
                print(line.strip())



def main():
    while True:
        print('\nКоманды для работы со справочником:\n'
              ' - Просмотр всех записей справочника: 1\n'
              ' - Поиск по справочнику: 2\n'
              ' - Добавление новой записи: 3\n'
              ' - Выход: 4')
        action = input('Выберите действие: ')
        if action == '1':
            read_file()
        elif action == '2':
            find_file()
        elif action == '3':
            write_file()
        elif action == '4':
            break
        else:
            print('Неверный ввод. Попробуйте еще раз.')


path_file = r'tel_book.txt'
if __name__ == '__main__':
    main()
