from django.contrib import admin

from .models import Pizza,Size
# Register your models here.

class MySize(admin.ModelAdmin):
    list_display = ("title",)


admin.site.register(Pizza)
admin.site.register(Size,MySize)