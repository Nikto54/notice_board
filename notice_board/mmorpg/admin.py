from django.contrib import admin
from .models import Category,Author,Notice,Response

admin.site.register(Category)
admin.site.register(Author)
admin.site.register(Notice)
admin.site.register(Response)