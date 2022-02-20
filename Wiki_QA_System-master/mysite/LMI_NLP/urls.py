from django.urls import path

from . import views
# < ... > get a part of the URL, before ":" is the type of the data got

app_name = 'LMI_NLP'
"""
# old views
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
"""
# question_id -> pk , add as.view()
urlpatterns = [
    #path('', views.IndexView.as_view(), name='index'),
    path('', views.RexanaMain.as_view(), name='Rexana'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),

    path('Execution.html',views.Execution )
]