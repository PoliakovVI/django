from django.db.models import *
from django.contrib.auth.models import User


class Note(Model):
    spent_time = FloatField()
    text = TextField(max_length=4096)
    created_at = DateTimeField('creation timestamp', auto_now_add=True)

    def __str__(self):
        return str(self.text) + " | " + str(self.spent_time)


class Comment(Model):
    note = ForeignKey(Note, on_delete=CASCADE)
    text = TextField(max_length=4096)
    created_at = DateTimeField('creation timestamp', auto_now_add=True)
    author = ForeignKey(User, on_delete=CASCADE, default=1)

    def __str__(self):
        return str(self.text)


class Record_request(Model):
    spent_time = FloatField()
    text = TextField(max_length=4096)
    created_at = DateTimeField('creation timestamp', auto_now_add=True)
    #document = FileField()

    def __str__(self):
        return str(self.text) + " | " + str(self.spent_time)
