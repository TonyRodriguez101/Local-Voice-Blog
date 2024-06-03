from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
# ListView hace una query a la base de datos de todos los elementos, Usamos para listar todos
# DetailView hace una query pero este trae solo una para ver todos los detalles, Usamos para visualizar 1
from .models import Post, Category
from .forms import PostForm, EditForm
from django.urls import reverse_lazy

# Create your views here.

#def home(request):
#    return render(request, 'home.html',{})


class HomeView(ListView):
    model = Post
    template_name= 'home.html'
    ordering =['-post_date']

class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_details.html'

class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    #fields = ('title','body')

class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'update_post.html'
    #fields = ['title','title_tag','body']

class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url= reverse_lazy('home')
    #fields = ['title','title_tag','body']



class AddCategoryView(CreateView):
    model = Category
    #form_class = PostForm
    template_name = 'add_category.html'
    fields= '__all__'
    #fields = ['name']


#funciones sin clases:
def CategoryView(request, cats):
    category_posts=Post.objects.filter(category=cats)
    return render(request, 'categories.html', {'cats':cats.title(), 'category_posts':category_posts})