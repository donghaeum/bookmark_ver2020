from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Bookmark
# Create your views here.
class BookmarkList(ListView):
    model = Bookmark
    paginate_by = 5
class BookmarkCreateView(CreateView):
    model = Bookmark
    fields = ['site_name', 'url']
    success_url = reverse_lazy('list')
class BookmarkDetailView(DeleteView):
    model = Bookmark
class BookmarkUpdateView(UpdateView):
    model = Bookmark
    fields = ['site_name', 'url']
    success_url = reverse_lazy('list')
    template_name_suffix = '_update'
class BookmarkDeleteView(DeleteView):
    model = Bookmark
    fields = ['site_name', 'url']
    success_url = reverse_lazy('list')