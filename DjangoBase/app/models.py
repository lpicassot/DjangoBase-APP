from django.db import models

# Create your models here.
class Product(models.Model):
    reference = models.CharField(
        unique=True,
        max_length=100,
        null=False,
        blank=False
    )
    name = models.CharField(
        max_length=250,
    )
    volume = models.CharField(
        max_length=60
    )
    created = models.DateTimeField(
        auto_now_add=True,
    )
    
    def __str__(self):
        return self.name