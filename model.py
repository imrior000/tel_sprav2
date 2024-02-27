import os
from copy import deepcopy
class PhoneBook:
    def __init__(self, path = 'phones.txt', sep = ';'):
        self.book = {}
        self.path = path
        self.sep = sep
        self.book_copy = None
    def copy_oryginal_book(self):
        self.book_copy = deepcopy(self.book)
    def open_phone_book(self):
        try:
            with open(self.path, 'r', encoding='utf-8') as file:
                data = file.readlines()
        except FileNotFoundError:
            with open(self.path, 'w+', encoding='utf-8') as file:
                data = file.readlines()
        for u_id, contact in enumerate(data, 1):
            self.book[u_id] = contact.strip().split(self.sep)
        self.copy_oryginal_book()
    def _next_id(self):
        return max(self.book) + 1 if self.book else 1
    def add_new_contact(self,data):
        self.book[self._next_id()] = data
    def find_contact(self, query):
        result = {}
        for u_id, contact in self.book.items():
            if query in ' '.join(contact):
                result[u_id] = contact
        return result
    def edit_contact(self,u_id,edited_contact):
        current_contact = self.book[u_id]
        for i in range(len(current_contact)):
            current_contact[i] = edited_contact[i] if edited_contact[i] else current_contact[i]
        self.book[u_id] = current_contact
        return current_contact[0]
    def check(string):
        try:
            float(string)
            return True
        except ValueError:
            return False
    def vybor_stroki(self, text, func):
        while True:
            u_id = func(text)
            if u_id.isdigit():
                return int(u_id)
    def delete_contact(self,u_id):
        return self.book.pop(u_id)[0]
    def save_book(self):
        data = []
        for contact in self.book.values():
            data.append(self.sep.join(contact))
        data = '\n'.join(data)
        with open(self.path, 'w', encoding='utf-8') as file:
            file.write(data)
    def save_backup(self):
        data = []
        for contact in self.book.values():
            data.append(self.sep.join(contact))
        data = '\n'.join(data)
        with open(self.path + '.back', 'w', encoding='utf-8') as file:
            file.write(data)
    def delete_backup(self):
        try:
            os.remove(self.path + '.back')
        except FileNotFoundError:
            pass
    def is_backup(self):
        try:
            with open(self.path + '.back', 'r', encoding='utf-8') as file:
                data = file.readlines()
        except FileNotFoundError:
            data = False
        return data
    def open_backup(self, data):
        for u_id, contact in enumerate(data, 1):
            self.book[u_id] = contact.strip().split(self.sep)
    def on_exit(self):
        if self.book_copy == self.book:
            return True
        return False
        
