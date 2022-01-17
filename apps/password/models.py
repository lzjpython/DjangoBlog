from django.db import models
from accounts.models import BlogUser


# Create your models here.

class PwdManager(models.Model):
    user = models.ForeignKey(BlogUser, on_delete=models.SET_NULL, null=True, verbose_name='用户')
    username = models.CharField(max_length=150, null=True, verbose_name='账号')
    pwd = models.CharField(max_length=150, null=True, verbose_name='密码')
    desc = models.CharField(max_length=150, null=True, verbose_name='简介')
    link = models.CharField(max_length=150, null=True, verbose_name='网站链接')
    is_delete = models.BooleanField(default=False, verbose_name='是否删除')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = '密码系统'
        verbose_name_plural = verbose_name
