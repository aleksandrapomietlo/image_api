import os
import shutil
from io import BytesIO
import random
import string

from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from users.models import AccountTier
from image.models import ExpiringLink, Image


def random_string(length=10):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for _ in range(length))


def create_temporary_image():
    from PIL import Image
    test_image_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'test-assets', 'dog.jpeg')
    with open(test_image_path, 'rb') as f:
        image_data = BytesIO(f.read())

    image = Image.open(image_data)
    image_file = BytesIO()
    image.save(image_file, format='JPEG')
    image_file.seek(0)

    return InMemoryUploadedFile(
        image_file,
        None,
        f'{random_string()}.jpg',  # Generate a random file name
        'image/jpeg',
        image_file.tell,
        None
    )


class ImageModelTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username=random_string(),
            email=f'{random_string()}@{random_string()}.com',
            password=random_string(),
            is_staff=True,
            is_active=True,
        )
        cls.image_file = create_temporary_image()
        cls.image = Image.objects.create(
            user=cls.user,
            image=cls.image_file,
        )

        cls.expected_image_name = random_string()
        cls.expected_ext = '.jpg'
        cls.expected_image_path = cls.image.get_orignal_url

    # ... (rest of the methods remain unchanged)


class ImageAPITestCase(APITestCase):
    def setUp(self):
        enterprise_account = AccountTier.objects.get(id=3)
        self.user = get_user_model().objects.create_user(
            username=random_string(),
            password=random_string(),
            account_tier=enterprise_account
        )
        self.client.login(username=self.user.username, password=self.user.password)
        self.image_file = create_temporary_image()

    # ... (rest of the methods remain unchanged)
