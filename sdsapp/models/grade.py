from django.db import models

class Grade(models.Model):

    name = models.CharField(max_length=55)

    class Meta:
        verbose_name = ("grade")
        verbose_name_plural = ("grades")

    def __str__(self):
        return self.name
        
    def get_absolute_url(self):
        return reverse("grade_detail", kwargs={"pk": self.pk})
    