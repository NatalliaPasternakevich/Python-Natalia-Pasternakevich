from django.urls import path
from . import views

app_name = 'reference_book'
urlpatterns = [
    path('ref-author-create/', views.CreateAuthor.as_view(), name='author-create'),
    path('ref-author/<int:pk>',views.ReadAuthor.as_view(), name='author-detail'),
    path('ref-author-update/<int:pk>',views.UpdateAuthor.as_view(), name='author-update'),
    path('ref-author-delete/<int:pk>',views.DeleteAuthor.as_view(), name='author-delete'),
    path('ref-author/',views.ShowAuthors.as_view(), name='author-show'),
    
    path('ref-seria-create/', views.CreateSeria.as_view(), name='seria-create'),
    path('ref-seria/<int:pk>',views.ReadSeria.as_view(), name='seria-detail'),
    path('ref-seria-update/<int:pk>',views.UpdateSeria.as_view(), name='seria-update'),
    path('ref-seria-delete/<int:pk>',views.DeleteSeria.as_view(), name='seria-delete'),
    path('ref-seria/',views.ShowSeria.as_view(), name='seria-show'),

    path('ref-genre-create/', views.CreateGenre.as_view(), name='genre-create'),
    path('ref-genre/<int:pk>',views.ReadGenre.as_view(), name='genre-detail'),
    path('ref-genre-update/<int:pk>',views.UpdateGenre.as_view(), name='genre-update'),
    path('ref-genre-delete/<int:pk>',views.DeleteGenre.as_view(), name='genre-delete'),
    path('ref-genre/',views.ShowGenre.as_view(), name='genre-show'),

    path('ref-publisher-create/', views.CreatePublisher.as_view(), name='publisher-create'),
    path('ref-publisher/<int:pk>',views.ReadPublisher.as_view(), name='publisher-detail'),
    path('ref-publisher-update/<int:pk>',views.UpdatePublisher.as_view(), name='publisher-update'),
    path('ref-publisher-delete/<int:pk>',views.DeletePublisher.as_view(), name='publisher-delete'),
    path('ref-publisher',views.ShowPublisher.as_view(), name='publisher-show'),
 
]