from django.db import models
from django.contrib.auth.models import User


class QuestionManager(models.Manager):
    def new(self):
        return self.order_by('-added_at')
    def popular(self):
        return self.order_by('-rating')


class Question(models.Model):
    title = models.CharField(max_length = 255)
    text = models.TextField()
    added_at = models.DateTimeField(blank=True, auto_now_add=True)
    rating = models.IntegerField(default=0)
    author = models.ForeignKey(User, related_name='que', on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name='question_like_user')
    objects = QuestionManager()


class Answer(models.Model):
    text = models.CharField(max_length = 255)
    added_at = models.DateTimeField(blank=True)
    question = models.ForeignKey(Question, related_name='quests', null=False, on_delete=models.CASCADE)
    author = models.ForeignKey(User, related_name='ans', on_delete=models.CASCADE)

