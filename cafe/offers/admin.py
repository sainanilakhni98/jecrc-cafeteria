from django.contrib import admin

# Register your models here.
from .models import Offer,Specials

admin.site.register(Offer)
admin.site.register(Specials)


