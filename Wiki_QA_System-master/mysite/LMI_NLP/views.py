from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.http import Http404
from django.template import loader
from .models import Question, Choice

"""
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'LMI_NLP/index.html', context)
"""


class IndexView(generic.ListView):
    template_name = 'LMI_NLP/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]


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

class DetailView(generic.DetailView):  # detailView expect primary key,so change views question_id to pk
    model = Question
    template_name = 'LMI_NLP/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'LMI_NLP/results.html'


"""
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)  # get_list_or_404() similar
    return render(request, 'LMI_NLP/detail.html', {'question': question})


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'LMI_NLP/results.html', {'question': question})
"""


# a link for race condition problem (two submision in the same time..)
# https://docs.djangoproject.com/en/4.0/ref/models/expressions/#avoiding-race-conditions-using-f

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'LMI_NLP/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        # redirect the user after the post,reverse() to avoid to hardcode the url
        return HttpResponseRedirect(reverse('LMI_NLP:results', args=(question.id,)))
