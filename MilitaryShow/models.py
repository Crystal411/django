from django.db import models

# Create your models here.

'''---存储用户名---'''
class UserInfo(models.Model):
    userName=models.CharField(u'用户名',max_length=20,primary_key=True)
    password=models.CharField(u'密码',max_length=20)
'''---存储图谱关系---'''
class KGStore(models.Model):
    fromId=models.CharField(u'关系起始',max_length=20)
    rel=models.CharField(u'关系',max_length=20)
    toId=models.CharField(u'关系终止',max_length=20)