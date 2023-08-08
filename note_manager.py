import json
from datetime import datetime

from note import Note


# создаем класс менеджера
class NoteManager:
    def __init__(self, filename):
        self.filename = "note.json"  # задаем имя файла для хранения заметок
        self.notes = []  # заметку записываем в виде словаря что бы было удобно парсить обратно
        self.load()

    # описание методов

    def add(self, title, body):  # добавление заметки
        note = Note(title, body)
        self.notes.append(note)  # добавляем в виде словаря
        return note.id

    def delete(self, note_id):  # передаем айди и перебором возвращаем нужную заметку
        for note in self.notes:
            if note.id == note_id:
                self.notes.remove(note)  # удвляем
                return True
        return False

    def update(self, note_id, title, body):  # передаем айди и находим перебором
        for note in self.notes:
            if note.id == note_id:
                note.update(title, body)  # перезаписываем поля методом из класса note
                return True
        return False

    def get(self, note_id=None):
        if note_id:
            for note in self.notes:
                if note.id == note_id:
                    return note  # получение заметки по айди
            return None
        else:
            return self.notes

    def load(self):
        try:
            with open(self.filename, "r") as f:
                data = json.load(f)  # открывем для чтения
                for note_data in data:
                    note = Note(note_data["title"], note_data["body"])
                    note.id = note_data["id"]
                    note.created_at = datetime.fromisoformat(note_data["created_at"])
                    note.updated_at = datetime.fromisoformat(note_data["updated_at"])
                    self.notes.append(note)
        except FileNotFoundError:
            pass

    def save(self):
        data = []  # создаем словарь
        for note in self.notes:
            data.append({  # записываем в него
                "id": note.id,
                "title": note.title,
                "body": note.body,
                "created_at": note.created_at.isoformat(),
                "updated_at": note.updated_at.isoformat()
            })
        with open(self.filename, "w") as f:
            json.dump(data, f)  # открываем и записываем в файл в джсоне
