from django.contrib import admin

# Register your models here.
from .models import Menu,FeedBack

admin.site.register(Menu)
admin.site.register(FeedBack)

