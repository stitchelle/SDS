from django.db import models
from .project import Project
from .dashboard import Dashboard

class SavedProject(models.Model):

    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    dashboard = models.ForeignKey(Dashboard, on_delete=models.CASCADE)
    note = models.CharField(max_length=255)

    class Meta:
        verbose_name = ("saved_project")
        verbose_name_plural = ("saved_projects")
    
    def __str__(self):
        return self.name
        
    def get_absolute_url(self):
        return reverse("saved_project_detail", kwargs={"pk": self.pk})
    