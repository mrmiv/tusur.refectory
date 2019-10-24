from django.db import models
from django.forms import ModelForm

# Create your models here.

# Модель еды (порции) с ее атрибутами
# class food_model(models.Model):
#     # название блюда
#     name = models.CharField(max_length=25, unique=True)
#     # общее количество порций (в шт/в граммах)
#     all_count = models.IntegerField()
#     # количество блюда. заказано порций в штуках
#     count = models.IntegerField(default=0)
#     # время заказа
#     # time = models.DateTimeField()
#     # цена порции (dp - разряд рублей, md - копейки )
#     price = models.DecimalField(decimal_places=3, max_digits=5)
#     # изображение блюда
#     # image = models.ImageField()

# class food(models.Model):
#     name = models.CharField(max_length=25)
#     price = models.DecimalField(decimal_places=2, max_digits=5, default=3)

# class shop(models.Model):
#     name = models.CharField(max_length=25)
#     price = models.DecimalField(decimal_places=2, max_digits=5, default=3)
#     count = models.IntegerField(default=1)


from django.db import models

# Блюдо
class product(models.Model):
    name = models.CharField(max_length=40)
    price = models.DecimalField(decimal_places=2, max_digits=5)
    category = models.CharField(max_length=25)
    #количество
    count = models.IntegerField(default=0)
      #состав
    structure = models.CharField(max_length=150)

# Пользователь
class user(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=35)

class Userform(ModelForm):
    class Meta:
        model = user
        fields = ['name', 'email', 'password']

# Заказы
class orders(models.Model):
    dateorder = models.DateField()
    timeorder = models.TimeField()
    pay = models.BooleanField()
    totalprice = models.DecimalField(decimal_places=2, max_digits=5)
    # статус выдачи
    deliverystatus = models.BooleanField()
    products = models.ManyToManyField(product)
    # Корпус выдачи:
    # building = CharField(max_length=5)

# Сотрудники
# username = EmailField()
# password = TextField()



