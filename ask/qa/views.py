from django.shortcuts import render
from django.http import HttpResponse 
from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_GET, require_http_methods
from qa.models import Question, Answer
from qa.forms import AskForm, AnswerForm, SignupForm, SigninForm
from django.core.paginator import Paginator, EmptyPage
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
from django.db.models import Max
from django.utils import timezone
import time

from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt



def import_data():

    res = Question.objects.all().aggregate(Max('rating'))
    max_rating = res['rating__max'] or 0
    user, _ = User.objects.get_or_create(
        username='x',
        defaults={'password':'y', 'last_login': timezone.now()})
    for i in range(30):
        question = Question.objects.create(
            title='question ' + str(i),
            text='text ' + str(i),
            author=user,
            rating=max_rating+i
        )
    time.sleep(2)
    question = Question.objects.create(title='question last', text='text', author=user)
    question, _ = Question.objects.get_or_create(pk=3141592, title='question about pi', text='what is the last digit?', author=user)
    question.answer_set.all().delete()
    for i in range(10):
        answer = Answer.objects.create(text='answer ' + str(i), question=question, author=user)


def test(request, *args, **kwargs):
    return HttpResponse('OK')


def paginate(request, qs):
    try:
        limit = int(request.GET.get('limit', 10))
    except ValueError:
        limit = 10
    if limit > 100:
        limit = 10
    try:
        page = int(request.GET.get('page', 1))
    except ValueError:
        raise Http404
    paginator = Paginator(qs, limit)
    try:
        page = paginator.page(page)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)
    return page

@require_GET
def init(request):
    
    import_data()  

    return render(request, 'qa/question.html', {
        'question': 'data imported',
    })

@require_GET
@login_required(login_url='/signin/')
def new(request):
    
    paginator = paginate(request, Question.objects.new())    

    return render(request, 'qa/questions.html', {
        'paginator': paginator,
    })

@require_GET
@login_required(login_url='/signin/')
def popular(request):
    
    paginator = paginate(request, Question.objects.popular())    

    return render(request, 'qa/questions.html', {
        'paginator': paginator,
    })

@csrf_exempt
@require_http_methods(["GET", "POST"])
@login_required(login_url='/signin/')
def question(request, *args, **kwargs):
    id = 0
    try:
        id = kwargs['id']
    except ValueError:
        raise Http404
    
    question = get_object_or_404(Question, id=id)
    answers =  Answer.objects.filter(question=question)
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            
            answer = form.save()
            url = question.get_url()
            return HttpResponseRedirect(url)
    else:
        form = AnswerForm(initial={'question': id})            
    return render(request, 'qa/question.html', {
        'question': question,
        'answers': answers,
        'form': form
    })

    
@csrf_exempt    
@require_http_methods(["GET", "POST"])
@login_required(login_url='/signin/')
def ask(request):
    if request.method == "POST":
        form = AskForm(request.POST)
        if form.is_valid():
            question = form.save()
            url = question.get_url()
            return HttpResponseRedirect(url)
    else:
        form = AskForm()
    return render(request, 'qa/ask.html', {
        'form': form
})
    
@csrf_exempt    
@require_http_methods(["GET", "POST"])
def signup(request):
    error = ''
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            try:
                user = form.save()
                login(request, user)
                return HttpResponseRedirect('/')
            except Exception as e:
                e_args = str(e).strip('()').split(',')
                if e_args[0] == '1062':
                    error = 'Пользователь уже существует'
                else:
                    error = ' Ошибка: ' + e_args[1]
        else:
            error = 'Не проканало'
    else:
        form = SignupForm()
    return render(request, 'qa/signup.html', {
        'form': form,
        'error': error,
        'url': 'signup',
                }
            )
    
        
    
@csrf_exempt    
@require_http_methods(["GET", "POST"])
def signin(request):
    error = ''
    logout(request)
    if request.method == "POST":
        form = SigninForm(request.POST)
        if form.is_valid():
            user = authenticate(
                request,
                username=request.POST.get('username', False),
                password=request.POST.get('password', False),
            )
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                error = 'Username or password is incorrect'
        else:
            error = 'Не проканало'
    else:
        form = SigninForm()
    return render(request, 'qa/signup.html', {
        'form': form,
        'error': error,
        'url': 'signin',
            }
        )
    
def logoff(request, *args, **kwargs):
    logout(request)
    return HttpResponseRedirect('/')