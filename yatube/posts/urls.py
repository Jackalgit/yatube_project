from django.urls import path

from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.index, name='index'),
    path('<slug>', views.group_posts, name='group_list'),
]
