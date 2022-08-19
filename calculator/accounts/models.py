from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model): #회원가입 할때 회원 정보들
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=10,null=True)
    major = models.CharField(max_length=10,null=True)
    ad_year = models.CharField(max_length=10,null=True)

    def __str__(self):
        return self.name or ''



class Lesson(models.Model): #User 객체에 수강한 과목들을 저장함.
    classname = models.CharField(max_length=50,null=True)
    classkind = models.TextField(max_length=10,null=True)
    classcredits = models.IntegerField(null=True)
    link = models.ForeignKey(User,on_delete=models.CASCADE,blank=True, null=True)

    def __str__(self):
        return self.classkind