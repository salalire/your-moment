from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Album

User = get_user_model()


class AlbumTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="user1",
            password="pass@123"
        )

    def test_create_album(self):
        album = Album.objects.create(
            owner=self.user,
            title="My Album"
        )

        self.assertEqual(album.title, "My Album")
        self.assertEqual(album.owner.username, "user1")