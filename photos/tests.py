from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse
from django.test import TestCase
from photos.models import Photo  
from django.contrib.auth import get_user_model
from albums.models import Album


User=get_user_model()

class PhotoUploadTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="user1",
            password="pass@123"
        )

        self.album = Album.objects.create(
            owner=self.user,
            title="Test Album"
        )

    def test_photo_upload(self):
        self.client.login(username="user1", password="pass@123")

        image = SimpleUploadedFile(
            name='test.jpg',
            content=b'file_content',
            content_type='image/jpeg'
        )

        response = self.client.post(
            reverse('upload_photo', args=[self.album.id]),
            {'image': image}
        )

        self.assertEqual(response.status_code, 302)
        self.assertEqual(Photo.objects.count(), 1)