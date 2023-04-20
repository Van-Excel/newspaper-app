from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import CustomUser
# Register your models here.


class CustomUserAdmin(UserAdmin):
    list_display = ["email", "username", "age", "is_staff"]
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + ((None, {"fields": ["age"]}),)
    add_fieldsets = UserAdmin.add_fieldsets + \
        ((None, {"fields": ["age"]}),)


admin.site.register(CustomUser, CustomUserAdmin)
