from django.db import models
from users.models import CustomUser
from todos.models import Todo

# Create your models here.
class Category(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    todo = models.ForeignKey(Todo, on_delete=models.CASCADE)
    subject = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.subject
