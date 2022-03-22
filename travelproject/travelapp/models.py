from django.db import models


# Create your models here.
class photos(models.Model):
    name = models.CharField(max_length=250)
    img = models.ImageField(upload_to='photo')
    des = models.TextField()

    def __str__(self):
        return self.name


class media(models.Model):
      name = models.CharField(max_length=250)
      img = models.ImageField(upload_to='medias')
      des = models.TextField()

      def __str__(self):
        return self.name
