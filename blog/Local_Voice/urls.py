
from django.urls import path
# from . import views
from .views import LikeView, HomeView,CategoryListView, CategoryView, AddCategoryView, ArticleDetailView,DeletePostView, AddPostView,UpdatePostView


urlpatterns = [
   # path('',views.home,name="home"),
    path('',HomeView.as_view(), name="home"),
    path('article/<int:pk>',ArticleDetailView.as_view(),name='article-detail'),
    # article/<int:pk> es como un url con un parametro. int:pk simboliza la primary key del articulo que seleccionamos
    path('add_post/',AddPostView.as_view(), name='add_post'),
    path('article/edit/<int:pk>',UpdatePostView.as_view(), name='update_post'),
    path('article/<int:pk>/remove',DeletePostView.as_view(), name='delete_post'),
    path('add_category/',AddCategoryView.as_view(), name='add_category'),
    path('category/<str:cats>/', CategoryView, name='category'),
    path('category-list/', CategoryListView, name='category-list'),
    path('like/<int:pk>', LikeView, name='like_post'),

]