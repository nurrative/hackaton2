from django.contrib import admin
from .models import Cart, Cartitems, Payment

admin.site.register(Cart)
admin.site.register(Cartitems)
admin.site.register(Payment)