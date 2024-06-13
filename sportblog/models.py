from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.core.exceptions import ValidationError
from django.db.models import ImageField


# Create your models here.

STATUS = ((0, "Draft"), (1, "Published"))

class Homepage(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

def validate_image_dimensions(Image):
    min_width = 1000
    min_height = 500
    img = Image.open(image)
    width, height = img.size

    if width < min_height or height < min_height:
        raise ValidationError(
            f"Image dimensions must be at least {min_width}px wide and {min_height}"
            )

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title