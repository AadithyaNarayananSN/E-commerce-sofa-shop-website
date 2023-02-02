from django.contrib import admin

# Register your models here.

from .models import *


admin.site.register(regmodel)
admin.site.register(productmodel)
admin.site.register(cartmodel)
admin.site.register(wishlistmodel)
admin.site.register(buymodel)
