from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.http import Http404
from django.template import loader
from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'LMI_NLP/index.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)  # get_list_or_404() similar
    return render(request, 'LMI_NLP/detail.html', {'question': question})

# try except written in hand
# def detail(request, question_id):
#     try:
#         question = Question.objects.get(pk=question_id)
#     except Question.DoesNotExist:
#         raise Http404("Question does not exist")
#     return render(request, 'LMI_NLP/detail.html', {'question': question})

# old detail function non used
# def detail(request, question_id):
#     return HttpResponse("You're looking at question %s." % question_id)



def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
