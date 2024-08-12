from django.db import models
from django.contrib.auth.models import AbstractUser
from django_resized import ResizedImageField
# Create your models here.

class User(AbstractUser):
    profile_image = ResizedImageField(
        size=[500, 500],
        crop=['middle' , 'center'],
        upload_to='profile'
    )

    followings = models.ManyToManyField('self', related_name='followers', symmetrical=False)    # 맞팔이 아닌 경우도 있음.

    # post_set = 
    # user_set = 
    # like_posts = 
    # followers = 
