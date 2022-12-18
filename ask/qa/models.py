from django.db import models
from django.contrib.auth.models import User
# from datetime import datetime

# class Post(models.Model):
#     title = models.CharField(max_length=255)
#     content = models.TextField()
#     creation_date = models.DateTimeField(blank=True)
#     def __unicode__(self):
#         return self.title
#     def get_absolute_url(self):
#         return '/post/%d/' % self.pk
#     class Meta:
#         db_table = 'blogposts'
#         ordering = ['-creation_date']

class QuestionManager(models.Manager):                                          
    def new(self):
        return self.order_by('-added_at')

    def popular(self):
        return self.order_by('-rating')
        
class Question(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    likes = models.ManyToManyField(User, related_name='likes_set')
    objects = QuestionManager() 
        

class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
    question = models.ForeignKey(Question, null=True, on_delete=models.SET_NULL)
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    
