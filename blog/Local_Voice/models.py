from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        #return reverse('article-detail', args=(str(self.id)))
        return reverse('home')


class Post(models.Model):
    title = models.CharField(max_length=255)
    #header_image = models.ImageField(null=True, blank=True, upload_to="images/")
    title_tag = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    #body = RichTextField(blank=True, null=True)
    body = models.TextField()
    post_date = models.DateField(auto_now_add=True)
    category = models.CharField(max_length=255, default='coding')
    #likes = models.ManyToManyField(User, related_name='blog_posts')



    def __str__(self):
        return self.title + ' | ' + str(self.author) # nos permitira desde la terminal de admin ver el titulo y el autor en vez de una string de numeros randoms como identificador de post.
    

    def get_absolute_url(self):
        return reverse('home')