# -*- coding: utf-8 -*-
from django import forms
from qa.models import Question, Answer, User
from django.db import IntegrityError
from django.contrib.auth.hashers import make_password
from django.contrib.auth.password_validation import validate_password
from django.conf import settings

class AskForm(forms.Form):
    """
    форма добавления вопроса
    """
    title = forms.CharField(max_length=100)
    text = forms.CharField(widget=forms.Textarea)
    
    
    def clean(self):
        if False:
            raise forms.ValidationError(
                u'Какая-то ошибка',
                code='err'
    )
            
    def save(self):
        question = Question(**self.cleaned_data)
        question.save()
        return question
            


class AnswerForm(forms.Form):
    """
    форма добавления ответа
    """
    text = forms.CharField(widget=forms.Textarea)
    question = forms.IntegerField(widget=forms.HiddenInput())
    def clean(self):
        if False:
            raise forms.ValidationError(
                u'Какая-то ошибка',
                code='err'
    )
            
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
        # try: 
        #     user.save()
        #     return user
        # except IntegrityError as e:
        #     raise Exception(e)
        user.save()
        return user
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