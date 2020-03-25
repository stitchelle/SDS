from django.db import models
from .teacher_parent import Teacher_Parent

class Dashboard(models.Model):

    name = models.CharField(max_length=55)
    teacher_parent = models.ForeignKey(Teacher_Parent, on_delete=models.CASCADE)

    class Meta:
        verbose_name = ("dashboard")
        verbose_name_plural = ("dashboards")
    
    def __str__(self):
        return self.name
        
    def get_absolute_url(self):
        return reverse("dashboard_detail", kwargs={"pk": self.pk})
    