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



