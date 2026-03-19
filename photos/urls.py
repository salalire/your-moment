from django.urls import path
from . import views
from django.urls import path
from . import views

urlpatterns = [

    path("upload/<int:album_id>/", views.upload_photo, name="upload_photo"),

]