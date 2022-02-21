from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.http import Http404
from django.template import loader
from .models import Question, Choice, QuestionForm,Top3Results
from .src import Application


"""
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'LMI_NLP/index.html', context)
"""


class RexanaMain(generic.ListView):
    template_name = 'LMI_NLP/Rexana.HTML'
    # template_name = 'LMI_NLP/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]



class DetailView(generic.DetailView):  # detailView expect primary key,so change views question_id to pk
    model = Question
    template_name = 'LMI_NLP/detail.html'

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.ListView):
    model = Top3Results
    template_name = 'Rexana.html'

class YourQuestion(generic.ListView):
    template_name = 'your-question.html'


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


def Execution(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            # cleaned data in form.cleaned_data
            Top3Response = Application.SiteMain(form.cleaned_data["Question"])
            return HttpResponseRedirect('/')  # needs a page to add the responses
    else:
        form = QuestionForm()
    return render(request, 'LMI_NLP/Execution.html', {'form': form})
