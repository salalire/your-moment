from django.urls import path
from . import views
urlpatterns = [
    path('create-album/', views.create_album, name='create_album'),
    # path('delete-album/<int:album_id>/', views.delete_album, name='delete_album'),
    path('list-albums/', views.my_albums, name='list_albums'),
    path("album/<int:album_id>/", views.album_detail, name="album_detail"),
    ]       