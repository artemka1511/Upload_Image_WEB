from django.db import models
import datetime


def user_directory_path(instance, filename):
    time = datetime.datetime.today().strftime("%d.%m.%Y_%H:%M:%S")
    return '{}_{}'.format(time, filename)


class UploadImage(models.Model):
    image = models.ImageField(upload_to=user_directory_path)
