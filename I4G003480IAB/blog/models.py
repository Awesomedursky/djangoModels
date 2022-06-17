from pyexpat import model
from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

# Create your models here.

class current_user_model(models.Model):
    name = models.CharField(max_length=150)




class Post(models.Model):
    Title = models.CharField(max_length=200)
    Text = models.TextField()
    Author = models.ForeignKey(current_user_model,on_delete = models.CASCADE,)
    Created_date = models.DateTimeField(auto_now_add=True)
    Published_date = models.DateTimeField(auto_now_add=True)
