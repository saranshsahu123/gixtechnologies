from django.db import models

class Applicant(models.Model):
    name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    feedback = models.TextField(blank=True, null=True)  # keep feedback

    def __str__(self):
        return self.name
