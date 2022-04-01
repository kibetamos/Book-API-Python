from django.contrib import admin
from .models import Book

# Register your models here.
admin.site.register(Book)
# we  have enabaled our admin page be able to view the model book and we can inputs to the database om the admin
