from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    title=models.CharField(max_length=255)
    author=models.ForeignKey(User, on_delete=models.CASCADE) #esto sirve para si eliminamos un usuario borrara todos sus post.
    body=models.TextField()


    def __str__(self):
        return self.title + ' | ' + str(self.author) # nos permitira desde la terminal de admin ver el titulo y el autor en vez de una string de numeros randoms como identificador de post.
    