from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Teacher_Parent(models.Model):

    # Important: Never define your own User in a Django app. Seriously. Never. Always extend it. In this application, we are creating a seperate model and making a one-to-one relationship between it and the built-in User.

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    is_teacher = models.BooleanField(null=True)


# These receiver hooks allow you to continue to
# work with the `User` class in your Python code.

# Every time a `User` is created, a matching `Teacher_Parent`
# object will be created and attached as a one-to-one
# property
@receiver(post_save, sender=User)
def create_teacher_parent(sender, instance, created, **kwargs):
    if created:
        Teacher_Parent.objects.create(user=instance)

# Every time a `User` is saved, its matching `Teacher_Parent`
# object will be saved.
@receiver(post_save, sender=User)
def save_teacher_parent(sender, instance, **kwargs):
    instance.teacher_parent.save()

    class Meta:
        verbose_name = ("teacher_parent")
        verbose_name_plural = ("teacher_parents")

    def __str__(self):
        return self.name
        
    def get_absolute_url(self):
        return reverse("teacher_parent_detail", kwargs={"pk": self.pk})
    