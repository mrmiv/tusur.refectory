from django.contrib import admin
from .models import order, basket

class inline_basket(admin.StackedInline):
    model = order.products.through

class basketadmin(admin.ModelAdmin):
    inlines = (inline_basket, )

admin.site.register(order, basketadmin)

# admin.site.register(order)
# admin.site.register(basket)
