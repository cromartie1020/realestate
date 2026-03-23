from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='home'),
    path('books/', views.book_list, name='book_list'),
    path('books/<int:id>/', views.book_detail, name='book_detail'),
]
