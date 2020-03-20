from django.db import models
from .instruction import Instruction
from .grade import Grade
from .subject import Subject
from .instruction import Instruction 
from .grade import Grade
from .subject import Subject
from .teacher_parent import Teacher_Parent


class Project(models.Model):

    # If two models are related, you open the model that represents the table with the foreign key and add a ForeignKey field.
    name = models.CharField(max_length=55)
    instruction = models.CharField(max_length=500)
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    teacher_parent = models.ForeignKey(Teacher_Parent, on_delete=models.CASCADE)
    image_path = models.CharField(max_length=255, null=True)
    supplies_needed = models.CharField(max_length=255)
    description = models.CharField(max_length=255)

    class Meta:
        verbose_name = ("project")
        verbose_name_plural = ("projects")

    def __str__(self):
        return self.name
        
    def get_absolute_url(self):
        return reverse("project_detail", kwargs={"pk": self.pk})
    