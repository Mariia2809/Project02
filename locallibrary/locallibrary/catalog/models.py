from django.db import models
from django.core.validators import FileExtensionValidator



class Category (models.Model):
    name = models.CharField(max_length=100, help_text="Введите категории")
    def __str__(self):
        return self.name

class CastomUser (models.Model):
    username = models.CharField(max_length=254, verbose_name='Лoгин', unique=True, blank=False)
    email = models.CharField(max_length=254, verbose_name='Пoчтa', unique=True, blank=False)
    password = models.CharField(max_length=254, verbose_name='Пapoль', blank=False)
    role = models.CharField(max_length=254, verbose_name='Poль',
                            choices=(('admin', 'Администратор'), ('user', 'Пoльзователь')), default='user')

class Application(models.Model):
    title = models.CharField(max_length=200)
    summary = models.TextField(help_text="Опишите свою заявку ")
    STATUS_CHOICES = [
        ('N', 'Новая'),
        ('P', 'Принято в работу'),
        ('C', 'Выполнено')
    ]
    category = models.ForeignKey(Category, help_text='Выберите категорию', on_delete=models.CASCADE)
    photo_file = models.ImageField(max_length=254, upload_to='image/', validators=[FileExtensionValidator(['jpg', 'jpeg', 'png', 'bmp'])])
    status = models.CharField(max_length=254, verbose_name='Статус', choices=STATUS_CHOICES, default='N')
    date = models.DateTimeField(verbose_name='Дата добавления')
    user = models.ForeignKey(CastomUser, verbose_name='Пользователь', on_delete=models.CASCADE)


