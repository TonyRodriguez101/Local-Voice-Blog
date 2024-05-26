from django.shortcuts import render
from django.views.generic import ListView, DetailView
# ListView hace una query a la base de datos de todos los elementos, Usamos para listar todos
# DetailView hace una query pero este trae solo una para ver todos los detalles, Usamos para visualizar 1
from .models import Post

# Create your views here.

#def home(request):
#    return render(request, 'home.html',{})


class HomeView(ListView):
    model = Post
    template_name= 'home.html'

class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_details.html'