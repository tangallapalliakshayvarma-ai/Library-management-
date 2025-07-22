from django.contrib import admin
from django.urls import path
from library import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('add/', views.add_book, name='add_book'),
    path('view/', views.view_books, name='view_books'),
    path('search/', views.search_book, name='search_book'),
    path('manage/', views.manage_users, name='manage_users'),
]
