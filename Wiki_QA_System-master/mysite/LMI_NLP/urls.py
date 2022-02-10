from django.urls import path

from . import views
# < ... > get a part of the URL, before ":" is the type of the data got

app_name = 'LMI_NLP'

urlpatterns = [
    # ex: /LMI_NLP/
    path('', views.index, name='index'),
    # ex: /LMI_NLP/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /LMI_NLP/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /LMI_NLP/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]