import Note


def create_note(number):
    title = text_len_check(
        input('Введите заголовок заметки: '), number
    )
    body = text_len_check(
        input('Введите содержание заметки: '), number
    )
    return Note.Note(title=title, body=body)


def text_len_check(text, length):
    while len(text) <= length:
        print(f'Текст должен быть больше {length} символов\n')
        text = input('Введите текст: ')
    else:
        return text


def menu():
    print('\nЭто программа "Заметки". Подскажите, что вы хотите сделать:\n\n1 - Посмотреть все заметки в файле\n'
          '2 - Добавить заметку\n3 - Удалить заметку\n4 - Редактировать заметку\n5 - Выборка заметок по дате\n'
          '6 - Поиск заметки по id\n7 - Выход из программы\n\nВведите номер функции: ')


def goodbye():
    print("Большое спасибо, будем ждать вас снова!")