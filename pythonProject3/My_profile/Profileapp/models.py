from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    name = models.name = models.CharField(default='Somesh Verma (Default)', max_length=200, null = True)

    title = models.CharField(default='This is the default,title change it in profile', max_length= 200, null = True)

    desc_text = 'Hey there is a default text discription about you that you can change on after clicking on "Edit"'

    desc = models.CharField(default= desc_text, max_length=200, null = True)

    profile_img = models.ImageField(default= 'media/default.jpg', upload_to='', null = True, blank = True)

    def __str__(self):
        return f"{self.user.username}'s profile "
