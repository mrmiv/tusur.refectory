from django.db import models

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

# product это блюдо
class product(models.Model):
    name = models.CharField(max_length=40)
    price = models.DecimalField(decimal_places=2, max_digits=5, default=3)
    category = models.CharField(max_length=25)
    #количество
    count = models.DecimalField(decimal_places=2, max_digits=5, default=3)
      #состав
    structure = models.CharField(max_length=150)

# Пользователь
class user(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()

# Заказы
class orders(models.Model):
    dateorder = models.DateField()
    timeorder = models.TimeField()
    Pay = models.BooleanField()
    totalprice = models.IntegerField()
    # статус выдачи
    deliverystatus = models.BooleanField()
    # Корпус выдачи: здесь сомнения у меня
    # building = CharField(max_length=5)

# Корзина ???? 

# Сотрудники
# username = EmailField()
# password = TextField()



