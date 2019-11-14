from django.db import models
from user_auth.models import ExtUser as user
from menu.models import product
# import staff member
from django.db.models.signals import pre_save, post_save, m2m_changed
from django.dispatch import receiver

class order(models.Model):

    total_price = models.DecimalField(decimal_places=2, max_digits=5, default=0)
    status_pay = models.BooleanField(default=False)
    status_get = models.BooleanField(default=False) 
    user = models.ForeignKey(user, on_delete=models.CASCADE)
    # staff_id = models.ForeignKey(staff_member, on_delete=models.PROTECT)
    time = models.DateTimeField(auto_now_add=True)
    basket = models.ManyToManyField(product)
    
    class Meta:
        ordering = ["id"]
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"

def get_total_price(sender, instance, **kwargs):
        instance.total_price = 0
        for prod in instance.basket.all():
            instance.total_price += prod.price
            # print(instance.total_price)
        instance.save()

m2m_changed.connect(get_total_price, sender=order.basket.through)