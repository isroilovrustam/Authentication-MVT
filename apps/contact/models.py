from django.db import models


# Create your models here.

class Contact(models.Model):
    full_name = models.CharField(max_length=202)
    email = models.EmailField()
    message = models.TextField()

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.full_name
