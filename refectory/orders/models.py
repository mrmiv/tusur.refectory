from django.db import models
from user_auth.models import ExtUser as user
from menu.models import product
# import staff member
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver

class order(models.Model):

    total_price = models.DecimalField(decimal_places=2, max_digits=5, default=0)
    status_pay = models.BooleanField(default=False)
    status_get = models.BooleanField(default=False)
    user_id = models.ForeignKey(user, on_delete=models.CASCADE)
    # staff_id = models.ForeignKey(staff_member, on_delete=models.PROTECT)
    time = models.DateTimeField()
    basket = models.ManyToManyField(product)
    
    class Meta:
        ordering = ["id"]
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"