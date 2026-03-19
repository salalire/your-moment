from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from albums.models import Album
from .models import Photo

@login_required
def upload_photo(request, album_id):

    album = get_object_or_404(Album, id=album_id)

    if request.method == "POST":

        image = request.FILES.get("image")
        caption = request.POST.get("caption")

        Photo.objects.create(
            album=album,
            image=image,
            caption=caption
        )

        return redirect("album_detail", album_id=album.id)

    return render(request, "photos/upload_photo.html", {"album": album})
