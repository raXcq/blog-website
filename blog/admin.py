from django.contrib import admin
from .models import Post # User

# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "body")

admin.site.register(Post, PostAdmin)

# class UserAdmin(admin.ModelAdmin):
#     list_display = (
#         "username",
#         "first_name",
#         "last_name",
#         "email",
#         "is_staff",
#         "is_active",
#         "is_superuser",
#     )

# admin.site.register(User, UserAdmin)
