from django.utils import timezone
from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    pass

class Category(models.Model):
    subject = models.CharField(max_length=100)

    class Meta:
        verbose_name = ('Category')
        verbose_name_plural = ('Categories')    
        
    def __str__(self):
        return self.subject

class Todo(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    # categories = models.ManyToManyField(Category, through='CategoryItem', related_name='tasks')
    categories = models.ManyToManyField(Category)
    title = models.CharField(max_length=200)
    body = models.TextField(blank=True)
    done = models.BooleanField(default=False)
    created_at = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))
    due_date = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated_at'] # ordering by updated field
    
    def __str__(self):
        return self.title # name to be shown when called
        