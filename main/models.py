from django.db import models

class Food(models.Model):
    name=models.CharField(max_length=50)
    description=models.TextField(max_length=100)
    
    def __str__(self):
        return self.name
