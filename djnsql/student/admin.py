from django.contrib import admin
from student.models import Profile

# Register your models here.

# admin.site.register(Profile)   #single register data

@admin.register(Profile)  # use 1
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id','name','email','city')

# admin.site.register(Profile,ProfileAdmin) # use 2

