import uuid
from datetime import datetime

#создаем класс заметки и задаем поля, после джавы тяжеловато переделывать на питон
class Note:
    def __init__(self, title, body):
        self.id = str(uuid.uuid4())#айдишник задается автоматически
        self.title = title
        self.body = body
        self.created_at = datetime.now()#ссылка на текущее время
        self.updated_at = datetime.now()

    def update(self, title, body):
        self.title = title
        self.body = body
        self.updated_at = datetime.now()

    #вывод заметки в консоль
    def __str__(self):
        return f"ID: {self.id}\nЗаголовок: {self.title}\nСодержание: {self.body}\nСоздание: {self.created_at}\nИзменения: {self.updated_at}\n"
