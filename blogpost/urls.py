from django.urls import path

from blogpost.apps import NewappConfig
from blogpost.views import BlogCreateView, BlogListView, BlogDetailView, BlogUpdateView, BlogDeleteView

app_name = NewappConfig.name

urlpatterns = [
    path('create/', BlogCreateView.as_view(), name='create'),
    path('', BlogListView.as_view(), name='list'),
    path('view/<int:pk>/', BlogDetailView.as_view(), name='view'),
    path('edit/<int:pk>/', BlogUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>/', BlogDeleteView.as_view(), name='delete'),
]
