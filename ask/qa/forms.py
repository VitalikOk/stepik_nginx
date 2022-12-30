# -*- coding: utf-8 -*-
from django import forms
from qa.models import Question, Answer
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth.hashers import make_password
from django.contrib.auth.password_validation import validate_password
from django.conf import settings

class AskForm(forms.Form):
    """
    форма добавления вопроса
    """
    def __init__(self, user, *args, **kwargs):
        self._user = user
        super(AskForm, self).__init__(*args, **kwargs)
            
    title = forms.CharField(max_length=100)
    text = forms.CharField(widget=forms.Textarea)
    author = forms.CharField(max_length=50, required=False)
    
    def clean(self):
        if False:
            raise forms.ValidationError(
                u'Какая-то ошибка',
                code='err'
    )
            
    def save(self):
        self.cleaned_data['author'] = User.objects.get(username=self._user)
        question = Question(**self.cleaned_data)
        question.save()
        return question

            


class AnswerForm(forms.Form):
    """
    форма добавления ответа
    """
    text = forms.CharField(widget=forms.Textarea)
    question = forms.IntegerField(widget=forms.HiddenInput())
    author = forms.CharField(max_length=50, required=False)
    def clean(self):
        if False:
            raise forms.ValidationError(
                u'Какая-то ошибка',
                code='err'
    )
            
    def clean_author(self):
        author = self.cleaned_data['author']
        try:
            author = User.objects.get(username=author)
        except:
            return None
        return author    
            
    def save(self):
        question = Question.objects.get(id=self.cleaned_data['question'])
        answer = Answer(text=self.cleaned_data['text'],question=question)
        answer.save()
        return answer
    
    
class SignupForm(forms.Form):
    """
    форма для регистрации
    """
    username = forms.CharField(max_length=20)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())
    
    def clean(self):
        if False:
            raise forms.ValidationError(
                u'Какая-то ошибка',
                code='err'
    )
            
    def clean_password(self):
        password = self.cleaned_data['password']
        # validate_password(password)
        password = make_password(password, salt=settings.SECRET_KEY)
        return password        
            
            
    def save(self):
        user = User(**self.cleaned_data)
        try: 
            user.save()
            return user
        except IntegrityError as e:
            raise Exception(e)
class SigninForm(forms.Form):
    """
    форма для логина
    """
    username = forms.CharField(max_length=20)
    password = forms.CharField(widget=forms.PasswordInput())
    
    def clean(self):
        if False:
            raise forms.ValidationError(
                u'Какая-то ошибка',
                code='err'
    )