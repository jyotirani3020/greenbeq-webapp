from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse, reverse_lazy
from ckeditor.fields import RichTextField

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    title = models.CharField(max_length = 200)
    #text = models.TextField()
    text = RichTextField(blank=True, null=True)
    blog_image = models.ImageField(blank=True, null=True, upload_to= "blog_images/",default='blog_images/image_1.jpg')
    created_date = models.DateTimeField(default = timezone.now())
    published_date = models.DateTimeField(blank = True, null = True)
    
    blog_category = models.CharField(max_length = 200, default='events')
    likes = models.ManyToManyField(User, related_name = 'blog_posts')
    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def total_likes(self):
        return self.likes.count()
    
   

    def get_absolute_url(self):
        return reverse("post_detail",kwargs={'pk':self.pk})


class BlogCategory(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("home")
