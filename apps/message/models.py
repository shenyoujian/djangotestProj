from django.db import models

# Create your models here.


class UserMessage(models.Model):
    name = models.CharField(max_length=20, null=True, blank=True, verbose_name=u'用户名')
    email = models.EmailField(verbose_name=u'邮箱')
    address = models.CharField(max_length=100, verbose_name=u'联系地址')
    message = models.CharField(max_length=500, verbose_name=u'留言信息')
    object_id = models.CharField(primary_key=True, max_length=50, default="", verbose_name=u"主键")

    class Meta:
        verbose_name = u"用户留言信息"
        ordering = '-object_id'
        verbose_name_plural = u"用户留言信息"
