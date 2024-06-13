from django.db import models
from django.contrib.auth.models import User

# Create your models here.

STATUS = ((0, "Draft"), (1, "Published"))

class Homepage(models.Model):
    title = models.CharField(max_length=150, unique=True)
    sub_title = models.CharField(max_length=200, unique=True)
    description = models.TextField(null=True, blank=True)
    bg_image = ImageField(upload_to='images/%Y/%m/%D', validators=[validate_image_dimensions])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models-DateTimeField(auto_now=True)

    def __str__(self):
        return self.title



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