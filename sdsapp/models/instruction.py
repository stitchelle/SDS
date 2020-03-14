from django.db import models

class Instruction(models.Model):

    step_detail = models.CharField(max_length=55)
    

    class Meta:
        verbose_name = ("instruction")
        verbose_name_plural = ("instructions")

    def __str__(self):
        return self.name
        
    def get_absolute_url(self):
        return reverse("instruction_detail", kwargs={"pk": self.pk})
    