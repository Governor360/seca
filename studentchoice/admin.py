from django.contrib import admin
from studentchoice.models import *

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'picture', 'details',]



admin.site.register(Appinfo)
admin.site.register(Category, CategoryAdmin)


