from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import MyUser,Hotelbook,Tickbooking
from .forms import UserForm

class UserAdmin(BaseUserAdmin):
    ordering = ['email']
    list_display=['name','email']
    list_filter = ('is_staff', 'is_superuser', 'groups')
    add_form = UserForm
    add_fieldsets = (
            (
                None,
                {
                    'classes': ('wide',),
                    'fields': ('name', 'email', 'password'),
                },
            ),
        )
    fieldsets = [
        (
            None,
            {
                'fields': ('name', 'email', 'password','points'),
            },
        ),
    ]

admin.site.register(MyUser, UserAdmin)
admin.site.register(Hotelbook)
admin.site.register(Tickbooking)

# Register your models here.
