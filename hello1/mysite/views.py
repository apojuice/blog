from django.shortcuts import render,get_object_or_404
from .models import Question
from django.http import HttpResponse,Http404





# Create your views here.

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list': latest_question_list
    }
    return render(request, 'mysite/index.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    return render(request, 'mysite/detail.html', {'question': question})

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse('You are voting on question %s.' % question_id)