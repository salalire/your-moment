from django.db import models
from albums.models import Album
class Photo(models.Model):
    caption = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='photos/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='photos')
    def __str__(self):
        return self.caption if self.caption else f"Photo {self.id}"


