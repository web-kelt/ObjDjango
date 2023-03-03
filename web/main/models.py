from django.contrib.auth.models import User
from django.db import models


class Object(models.Model):
    object_name = models.TextField('Объект учёта', max_length=50)
    object_people = models.TextField('Ответственное лицо', max_length=50)
    object_cabinet = models.IntegerField('Номер кабинета')

    def __str__(self):
        return self.object_name

