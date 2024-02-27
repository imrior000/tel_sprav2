main_menu = ['Главное меню',
             'Показать контакты',
             'Найти контакт',
             'Создать контакт',
             'Сохранить изменения',
             'Выход']
podmenu = ['С выбранным',
             'Изменить',
             'Удалить',
             'Вернуться в главное меню']
privet = "Вас приветствует теелфонный справочник v0.2b"
choice_main_menu = f'Выберите пункт меню (1 - {len(main_menu)-1}) : '
choice_podmenu = f'Выберите пункт меню (1 - {len(podmenu)-1}) : '
choice_main_menu_error = f'Нужно ввести число от 1 до {len(main_menu)-1}'
choice_podmenu_error = f'Нужно ввести число от 1 до {len(podmenu)-1}'
phone_book_opened_successful = 'Телефонная книга открыта успешно!'
phone_book_saved_successful = 'Телефонная книга сохранена успешно!'
input_new_contact = ['Введите имя контакта : ', 'Введите номер контакта : ', 'Введите комментарий для контакта : ']
input_search_data = 'Введите фразу для поиска : '
edit_contact_text = ['Введите новое имя','Введите новый номер','Введите новый комментарий']
vybor_kontakta = 'Введите номер строки (0 - для возврата в главное меню) : '
pustaya_kniga = 'Телефонная книга пуста!'
xxx_exit = 'Обнаружено неправильное закрытие программы, загрузить последнее сохраненное изменение?(y/n)'
prov_yn = 'Введите y или n : '
exit_changes = 'Есть не сохраненные изменения, сохранить? (y/n) : '
phone_book_no_saved = 'Изменения не сохранены...'

def delete_confirm(name):
    return f"Точно удалить контакт {name}? (y/n) : "
def new_contact_added_successful(name):
    return f'Контакт {name} успешно добавлен.'
def find_contact_no_result(word):
    return f'Контакты содержащие {word} - не найдены!'
def edit_contact(textes, names):
    ret = []
    for i in range(len(textes)):
        ret.append(f'{textes[i]} [{names[i]}] : ')
    return ret
def edit_contact_successful(name):
    return f'Контакт {name} успешно изменен.'
def delete_contact_successful(name):
    return f'Контакт {name} удален.'
def delete_contact_unsuccessful(name):
    return f'Контакт {name} не удален.'