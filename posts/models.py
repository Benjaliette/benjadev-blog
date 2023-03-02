from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=128, null=False)
    content = models.TextField(blank=False)
    cover = CloudinaryField('image')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.title
