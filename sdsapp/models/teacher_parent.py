from django.db import models
from django.contrib.auth.models import User

class Teacher_Parent(models.Model):

    # Important: Never define your own User in a Django app. Seriously. Never. Always extend it. In this application, we are creating a seperate model and making a one-to-one relationship between it and the built-in User.

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    is_teacher = models.BooleanField(default=True)

    