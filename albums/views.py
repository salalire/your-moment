from django.shortcuts import render, redirect
from .forms import AlbumForm
from django.contrib.auth.decorators import login_required
from photos.models import Photo,Album
from django.shortcuts import get_object_or_404

@login_required
def create_album(request):
    if request.method == "POST":
        form = AlbumForm(request.POST)
        if form.is_valid():
            album = form.save(commit=False)
            album.owner = request.user
            album.save()
            return redirect("list_albums")
    else:
        form = AlbumForm()
    return render(request, "albums/create_album.html", {"form": form})


@login_required
def my_albums(request):

    albums = request.user.albums.all()

    return render(request, "albums/list_albums.html", {"albums": albums})

@login_required
def album_detail(request, album_id):

    album = get_object_or_404(Album, id=album_id)

    photos = album.photos.all()

    return render(request, "albums/album_detail.html", {
        "album": album,
        "photos": photos
    })
