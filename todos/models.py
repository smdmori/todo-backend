from django.utils import timezone
from django.db import models
from users.models import CustomUser
# from categories.models import Category

# class Category(models.Model):
#     subject = models.CharField(max_length=200)

#     class Meta:
#         verbose_name = ('Category')
#         verbose_name_plural = ('Categories')    
    
#     def __str__(self):
#         return self.subject

# Create your models here.
class Todo(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    # category = models.ManyToManyField(Category, blank=True)
    title = models.CharField(max_length=200)
    body = models.TextField(blank=True)
    done = models.BooleanField(default=False)
    created_at = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))
    due_date = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))

    class Meta:
        ordering = ['-created_at'] # ordering by created field
    
    def __str__(self):
        return self.title # name to be shown when called
