from django.contrib import admin
from .models import Todo, Category, CustomUser

admin.site.register(Todo)
admin.site.register(Category)
admin.site.register(CustomUser)