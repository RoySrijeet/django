from django.db import models

# Create your models here.

class Login(models.Model):
    username = models.CharField(max_length = 250)
    password = forms.CharField(max_length=32, widget=forms.PasswordInput) 