from django import forms
from qa.models import Question, Answer


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
    question_id = forms.IntegerField(widget=forms.HiddenInput())
    def clean(self):
        if False:
            raise forms.ValidationError(
                u'Какая-то ошибка',
                code='err'
    )
            
    def save(self):
        question = Question.objects.get(id=self.cleaned_data['question_id'])
        answer = Answer(text=self.cleaned_data['text'],question=question)
        answer.save()
        return answer