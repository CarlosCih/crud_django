from django.db import models

# Create your models here.
class Task(models.Model):
    title=models.CharField(max_length=50)
    description=models.TextField(blank=True)
    is_completed=models.BooleanField(default=False)
    created=models.DateTimeField(auto_now=True)

    class Meta:
        ordering=['-created']

    def __str__(self):
        return self.title