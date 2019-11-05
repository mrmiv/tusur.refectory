from django.db import models
from django.db.models.signals import pre_save, post_save, m2m_changed

class product(models.Model):
    CATEGORY_CHOICES = (
        ('1', 'Супы'),
        ('2', 'Гарниры'),
        ('2', 'Горячие блюда'),
        ('3', 'Салаты'),
        ('4', 'Завтраки'),
        ('5', 'Выпечка'),
        ('6', 'Дополнительно')
    )

    name = models.CharField(max_length=64)
    price = models.DecimalField(decimal_places=2, max_digits=5)
    category = models.CharField(max_length=64, choices=CATEGORY_CHOICES)
    count = models.IntegerField(default=1)
    total_count = models.IntegerField(default=10, editable=False)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ["name"]
        verbose_name = "Блюдо"
        verbose_name_plural = "Блюда"