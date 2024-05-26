from django.contrib import admin
from . models import Post
# Register your models here.

admin.site.register(Post) # Permite los blog post sean accedibles desde el area admin.
