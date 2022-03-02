from django.urls import path

from . import views

# < ... > get a part of the URL, before ":" is the type of the data got

app_name = 'LMI_NLP'

# question_id -> pk , add as.view()
urlpatterns = [
    # path('', views.IndexView.as_view(), name='index'),
    #path('', views.RexanaMain.as_view(), name='Rexana'),
    # path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('LMI_NLP/results.html', views.ResultsView.as_view(), name='results'),
    path('your-question.html',views.YourQuestion),
    # path('results/', views.ResultsView.as_view(), name='results'),
    # path('<int:question_id>/vote/', views.vote, name='vote'),
    path('Rexana.html',views.Rexana),
    path('Execution.html', views.Execution)
]
