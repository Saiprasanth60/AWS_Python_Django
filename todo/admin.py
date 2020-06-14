from django.contrib import admin
from .models import todo

# Register your models here.
class todoAdmin(admin.ModelAdmin):
    #readonly_fields - this make field perminent created on models with auto_now_add
    readonly_fields = ('created',)

admin.site.register(todo,todoAdmin)