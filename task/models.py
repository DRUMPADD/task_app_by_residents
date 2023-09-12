from django.db import models

# Create your models here.
class Tasks(models.Model):
    task_name = models.CharField(max_length=200, null=False)
    task_desc = models.CharField(max_length=200, null=False)

    class Meta:
        db_table = "Tasks"
    def __str__(self):
        return f'{self.pk}'