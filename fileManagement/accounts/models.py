from django.db import models
from cloudinary_storage.storage import RawMediaCloudinaryStorage

class User(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(default='default-for-user.png', upload_to='images/', blank=True)
    report = models.FileField(upload_to='raw/', blank=True, storage=RawMediaCloudinaryStorage())