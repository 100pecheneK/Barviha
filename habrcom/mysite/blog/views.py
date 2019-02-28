from django.shortcuts import render
from django.views.generic import ListView, DetailView
from blog.models import Post


class PostsListView(ListView):  # представление в виде списка
    model = Post  # модель для представления


class PostDetailView(DetailView):
    model = Post  # детализированное представление модели
