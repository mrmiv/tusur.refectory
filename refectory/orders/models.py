from django.db import models
from user_auth.models import ExtUser as user
from menu.models import product

# import staff member
from django.db.models.signals import m2m_changed, post_save
from django.dispatch import receiver

class order(models.Model):

    total_price = models.DecimalField(decimal_places=2, max_digits=8, default=0)
    status_pay = models.BooleanField(default=False)
    status_get = models.BooleanField(default=False) 
    user = models.ForeignKey(user, on_delete=models.CASCADE)
    # staff_id = models.ForeignKey(staff_member, on_delete=models.PROTECT)
    time = models.DateTimeField(auto_now_add=True)
    products = models.ManyToManyField(product, through='basket', through_fields=('order','product','quantity'))

    def get_total_price(self):
        self.total_price = 0
        items = basket.objects.filter(order=self)
        # print(items)
        for item in items:
            self.total_price += item.product.price*item.quantity
        # print(self.total_price)
        self.save()
        
    class Meta:
        ordering = ["id"]
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"

class basket(models.Model):
    order =  models.ForeignKey(order, verbose_name='Заказ', on_delete=models.CASCADE)
    product = models.ForeignKey(product, verbose_name='Товар',  on_delete=models.CASCADE)
    # дополнительно(FK)
    quantity = models.PositiveIntegerField(default=1, verbose_name='Количество')

    def __str__(self):
        return 'Заказ:{0}. Товар: {1} - {2}шт.'.format(self.order, self.product, self.quantity)

    class Meta:
        db_table = 'orders_order_products'
        verbose_name_plural = 'Продукты заказа'
        verbose_name = 'Продукт заказа'

# @receiver(m2m_changed, sender=basket)
# def get_total_price(sender,instance, **kwargs):
#     print('hello')
#     # this_order.save()
