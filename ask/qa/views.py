from django.shortcuts import render
from django.http import HttpResponse 
from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_GET
from qa.models import Question, Answer
from django.core.paginator import Paginator

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
def question(request):
    
    paginator = paginate(request, Question.objects.new())    

return render(request, 'qa/questions.html', {
        'paginator': paginator,
    })

@require_GET
def popular(request):
    
    paginator = paginate(request, Question.objects.popular())    

return render(request, 'qa/questions.html', {
        'paginator': paginator,
    })


@require_GET
def question(request, id):
    question = get_object_or_404(Question, id=id)
    try:
        answer = question.answer.filter(user=request.user)[0]
    except Vote.DoesNotExist:
        vote = None
    return render(request, 'qa/question.html', {
        'question':     question,
    })
    
    
    def post_details(request, slug):
    post = get_object_or_404(Post, slug=slug)

    return render(request, 'blog/post_details.html', {
        'post':     post,
        'category': post.category,
        'tags':     post.tags.all()[:],
        'vote':     vote,
})