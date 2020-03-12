from django.db import models

class Subject(models.Model):

    name = models.CharField(max_length=55)

    class Meta:
        verbose_name = ("subject")
        verbose_name_plural = ("subjects")

    def __str__(self):
        return self.name
        
    def get_absolute_url(self):
        return reverse("subject_detail", kwargs={"pk": self.pk})
    