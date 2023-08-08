from note_manager import NoteManager


class ConsoleInterface:
    def __init__(self, filename):
        self.note_manager = NoteManager(filename)

    def run(self):
        while True:
            self.print_menu()
            command = input("Введите номер команды: ")
            if command == "1":
                self.add_note()
            elif command == "2":
                self.delete_note()
            elif command == "3":
                self.update_note()
            elif command == "4":
                self.show_notes()
            elif command == "5":
                self.show_note()
            elif command == "6":
                self.note_manager.save()
                print("Заметка записана в файл")
            elif command == "7":
                break
            else:
                print("Некоректный ввод, попробуйте еще раз.")

    def print_menu(self):
        print("1. Создать заметку")
        print("2. Удалить заметку (знать номер id)")
        print("3. Изменить заметку по id")
        print("4. Показать все заметки")
        print("5. Вывести заметку по id")
        print("6. ЗАписать изменения в файл")
        print("7. Выход")

    def add_note(self):
        title = input("Введите название заголовка: ")
        body = input("Введите содержание заметки: ")
        note_id = self.note_manager.add(title, body)
        print(f"ЗАметка сохранена с номером ID {note_id}.")

    def delete_note(self):
        note_id = input("Введите ID заметки: ")
        if self.note_manager.delete(note_id):
            print(f"Заметка с ID {note_id} удалена.")
        else:
            print(f"ЗАметка с ID {note_id} не найдена.")

    def update_note(self):
        note_id = input("Введите ID заметки:")
        title = input("Введите новый заголовок: ")
        body = input("Введите новое содержание: ")
        if self.note_manager.update(note_id, title, body):
            print(f"Заметка с  ID {note_id} изменена.")
        else:
            print(f"Заметка с  ID {note_id} не найдена.")

    def show_notes(self):
        notes = self.note_manager.get()
        if notes:
            for note in notes:
                print(note)
        else:
            print("Заметки отсутсвуют.")

    def show_note(self):
        note_id = input("Введите ID заметки: ")
        note = self.note_manager.get(note_id)
        if note:
            print(note)
        else:
            print(f"Заметка с ID {note_id} не найдена.")