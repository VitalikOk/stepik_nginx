from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class QuestionManager(models.Manager):                                          
    def new(self):
        return self.order_by('-added_at')

    def popular(self):
        return self.order_by('-rating')
    
    def question(self, qid):
        return self.filter(id=qid)
        
class Question(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True, null=True)
    rating = models.IntegerField(default=0, null=True)
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    likes = models.ManyToManyField(User, related_name='likes_set', null=True)
    objects = QuestionManager() 
    

    
    def __unicode__(self):
        return self.title
    
    
    def get_url(self):
        return reverse('question', kwargs={'id': self.id})
    
    
    # def get_url(self):
    #     return reverse('blog:tag-details', kwargs={'slug': self.slug})
        

class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField(null=True)
    question = models.ForeignKey(Question, null=True, related_name='answer_set', on_delete=models.SET_NULL)
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    
    def __unicode__(self):
        return self.text
    
