import viev
import text
import model

def start_app():
    pb = model.PhoneBook()
    viev.show_message(text.privet)
    data = pb.is_backup()
    if data:
        prov = viev.input_data(text.xxx_exit)
        if viev.prov_yn(prov):
            pb.open_backup(data)
        else:
            pb.open_phone_book()
    else:
        pb.open_phone_book()
    viev.show_message(text.phone_book_opened_successful)
    while True:
        user_choice = viev.show_main_menu()
        match user_choice:
            case 1:
                if pb.book:
                    viev.show_contacts(pb.book)
                    u_id = pb.vybor_stroki(text.vybor_kontakta,viev.input_data)
                    if u_id == 0:
                        pass
                    else:
                        podmenu(u_id,pb)
                else:
                    viev.show_message(text.pustaya_kniga)
            case 2:
                search_word = viev.input_data(text.input_search_data)
                searched = pb.find_contact(search_word)
                if searched:
                    viev.show_contacts(searched, text.find_contact_no_result(search_word))
                    u_id = pb.vybor_stroki(text.vybor_kontakta,viev.input_data)
                    if u_id == 0:
                        pass
                    else:
                        podmenu(u_id,pb)
                else:
                    viev.show_message(text.find_contact_no_result(search_word))
            case 3:
                data = viev.input_data(text.input_new_contact)
                pb.add_new_contact(data)
                pb.save_backup()
                viev.show_message(text.new_contact_added_successful(data[0]))
            case 4:
                pb.save_book()
                viev.show_message(text.phone_book_saved_successful)
                pb.copy_oryginal_book()
            case 5:
                if pb.on_exit():
                    pass
                else:
                    ret = viev.input_data(text.exit_changes)
                    if viev.prov_yn(ret):
                        pb.save_book()
                        viev.show_message(text.phone_book_saved_successful)
                    else:
                        viev.show_message(text.phone_book_no_saved)
                pb.delete_backup()
                break
def podmenu(u_id,pb):
    while True:
        user_choice = viev.show_podmenu()
        match user_choice:
            case 1:
                data = viev.input_data(text.edit_contact(text.edit_contact_text,pb.book[u_id]))
                ret = pb.edit_contact(u_id,data)
                pb.save_backup()
                viev.show_message(text.edit_contact_successful(ret))
            case 2:
                name =pb.book[u_id][0]
                data = viev.input_data(text.delete_confirm(name))
                if viev.prov_yn(data):
                    ret = pb.delete_contact(u_id)
                    pb.save_backup()
                    viev.show_message(text.delete_contact_successful(name))
                else:
                    viev.show_message(text.delete_contact_unsuccessful(name))
                break
            case 3:
                break