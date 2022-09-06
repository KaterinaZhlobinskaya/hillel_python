def read_first_ten_lines():
    ln_number = lines_number()
    if ln_number < 10:
        return read_all_lines()[0:ln_number]
    else:
        return read_all_lines()[0:10]


def read_last_ten_lines():
    ln_number = lines_number()
    if ln_number < 10:
        return read_all_lines()[-ln_number:]
    else:
        return read_all_lines()[-10:]


def read_all_lines():
    lines = file.readlines()
    file.seek(0)
    return lines


def exit_func():
    file.close()
    exit()


def lines_number():
    return len(read_all_lines())


def words_frequency():
    words = dict()
    lines = read_all_lines()
    for line in lines:
        for word in line.split():
            word = clean_word(word).lower()
            if word in words:
                words[word] = words[word] + 1
            else:
                words[word] = 1
    return words


def find_longest_word():
    maxlen = 0
    longword = ""
    lines = read_all_lines()
    for line in lines:
        for word in line.split(" "):
            word = clean_word(word)
            if len(word) > maxlen:
                maxlen = len(word)
                longword = word

    return longword


def print_lines(lines):
    for line in lines:
        print(line, end="")


def print_dict(lines):
    for key in lines:
        print(key, " - ", lines[key])


def clean_word(word):
    return word.replace(' ', '').replace('.', '').replace(',', '')

path = input("Введите имя файла:")

try:
    file = open(path)
except:
    print("Не удалось прочитать файл")
    exit()
else:
    print_lines(read_all_lines())
    while 1:
        print("Выберите опцию:")
        print("1 - Прочитать первые 10 строк")
        print("2 - Прочитать последние 10 строк")
        print("3 - Прочитать весь текст")
        print("4 - Вывести количество строк")
        print("5 - Вывести длиннейшее слово")
        print("6 - Вывести число повторений")
        print("7 - Выход")
        a = input("Ваш выбор:")
        if a.isnumeric() and 8 > int(a) > 0:
            choise = int(a)
            if choise == 1:
                print_lines(read_first_ten_lines())
            elif choise == 2:
                print_lines(read_last_ten_lines())
            elif choise == 3:
                print_lines(read_all_lines())
            elif choise == 4:
                print(lines_number())
            elif choise == 5:
                print(find_longest_word())
            elif choise == 6:
                print_dict(words_frequency())
            else:
                exit_func()
        else:
            print("Выбор не распознан")