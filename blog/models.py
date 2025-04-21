from django.db import models
from django.urls import reverse

# Create your models here.


class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


# class User(models.Model):
#     user_id = models.AutoField(primary_key=True)
#     username = models.CharField(max_length=150, unique=True)
#     first_name = models.CharField(max_length=150)
#     last_name = models.CharField(max_length=150)
#     email = models.EmailField(unique=True)
#     password = models.CharField(max_length=128)
#     # groups = models.ManyToManyField('auth.Group', blank=True)
#     # user_permissions = models.ManyToManyField('auth.Permission', blank=True)
#     is_staff = models.BooleanField(default=False)
#     is_active = models.BooleanField(default=True)
#     is_superuser = models.BooleanField(default=False)
#     last_login = models.DateTimeField(null=True, blank=True)
#     date_joined = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.username

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.pk})
