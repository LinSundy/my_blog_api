from django.db import models


# Create your models here.
class UserInfo(models.Model):
    user_type_choices = (
        (1, '普通用户'),
        (2, 'vip'),
        (1, 'svip'),
    )
    user_type = models.IntegerField(choices=user_type_choices)
    username = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=50)


class UserToken(models.Model):
    user = models.OneToOneField(to='UserInfo', on_delete=models.DO_NOTHING)
    token = models.CharField(max_length=64)
