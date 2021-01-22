from django.shortcuts import render, HttpResponse
from django.template import loader
from django.http import Http404
from .models import Question
from django.shortcuts import render, get_object_or_404

# Create your views here.
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    #template = loader.get_template('polls/index.html')
    
    context={'latest_question_list':latest_question_list,

    }
    return render(request,'polls/index.html', context)

    #output = ', '.join([q.question_text for q in latest_question_list]) => put it on site directly with python code

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except:
        raise Http404("Question does not exist")

    return render(request, 'polls/detail.html',{'question':question})


def results(request, question_id):
    response = "You are looking at the results of question %s"
    return HttpResponse(response % question_id)

def vote(request, question_id):
    response = "You are voting on question %s"
    return HttpResponse(response % question_id)