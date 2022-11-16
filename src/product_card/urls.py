from django.urls import path
from . import views

app_name = 'product_card'
urlpatterns = [
    path('pcard-book-create/', views.CreateBook.as_view(), name='book-create'),
    path('pcard-book/<int:pk>',views.ReadBook.as_view(), name='book-detail'),
    path('pcard-book-update/<int:pk>',views.UpdateBook.as_view(), name='book-update'),
    path('pcard-book-delete/<int:pk>',views.DeleteBook.as_view(), name='book-delete'),
    path('pcard-book/',views.ShowBook.as_view(), name='book-show')
]