from django.urls import path
from . import views 

app_name = 'books'

urlpatterns = [
    # show all books
    path('', views.book_list , name='book_list'),
]