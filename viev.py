import text

def show_main_menu():
    for i, item in enumerate(text.main_menu):
        if i:
            print(f'\t{i}. {item}')
        else:
            print(item)
    while True:
        choice = input(text.choice_main_menu)
        if choice.isdigit() and 0 < int(choice) < len(text.main_menu):
            return int(choice)
        print(text.choice_main_menu_error)
def show_podmenu():
    for i, item in enumerate(text.podmenu):
        if i:
            print(f'\t{i}. {item}')
        else:
            print(item)
    while True:
        choice = input(text.choice_podmenu)
        if choice.isdigit() and 0 < int(choice) < len(text.podmenu):
            return int(choice)
        print(text.choice_podmenu_error)
def show_contacts(phone_book, error_message = "!"):
    if phone_book:
        print('\n' + '=' * 75)
        for u_id, contact in phone_book.items():
            print(f'{u_id:<3}. | {contact[0]:<20} | {contact[1]:<20} | {contact[2]:<20}')
        print('=' * 75 + '\n')
    else:
        show_message(error_message)
def show_message(message):
    print('\n' + '=' * len(message))
    print(message)
    print('=' * len(message) + '\n')
def input_data(mess):
    if isinstance(mess, str):
        return input('\n' + mess)
    else:
        return [input(message) for message in mess]
def prov_yn(yn):
    while True:
        if yn == "y":
            return True
        elif yn == "n":
            return False
        else:
            yn = input_data(text.prov_yn)
