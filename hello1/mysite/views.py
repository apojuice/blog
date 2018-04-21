from django.shortcuts import render,get_object_or_404,reverse
from .models import Question,Choice
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.utils import timezone
from django.views import generic



# Create your views here.

class IndexView(generic.ListView):
    template_name = 'mysite/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = 'mysite/detail.html'

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now())

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'mysite/results.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'mysite/detail.html',{
            'question': question,
            'error_message': "还没选中选项哦！",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
    return HttpResponseRedirect(reverse('mysite:results', args=(question.id,)))