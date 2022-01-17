from django.contrib import admin


# Register your models here.

class PwdAdmin(admin.ModelAdmin):
    list_display = ('username', 'pwd', 'desc')
