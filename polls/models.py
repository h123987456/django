from django.db import models
from django.utils import timezone
from datetime import  datetime, timedelta

# Create your models here.
class Question(models.Model):
    question_text = models.CharField('问题内容', max_length=200)
    pub_date = models.DateTimeField('发布时间')

    def __str__(self):  # (了解)控制打印对象时的输出信息
        return self.question_text

    def was_published_recently(self):
        if timezone.now() - timedelta(days=1) <= self.pub_date:
            return True
        else:
            return False


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField('选项内容', max_length=200)
    votes = models.IntegerField('投票数', default=0)

    def __str__(self):
        return self.choice_text

# django自带的orm框架，用法类似sqlalchemy
# 自定义的类 要继承orm框架中的model类，这样orm框架能把类和数据库联系起来