import datetime
from django.db import models
from django.utils import timezone
from django import forms


# we need to get the question
# sent the three answers of the question to the site
# apply changement in models : python manage.py makemigrations LMI_NLP
# see SQL command made to change the db : python manage.py sqlmigrate LMI_NLP 0001
# verify the conformity of the project: python manage.py check
# apply the changement in the db : python manage.py migrate

class Question(models.Model):
    def __str__(self):
        return self.question_text

    question_text = models.CharField(max_length=200)
    # first argument for changing name of the field
    pub_date = models.DateTimeField('date published')

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    # time in the future bugs
    # def was_published_recently(self):
    #     return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    def __str__(self):
        return self.choice_text

    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)


class QuestionForm(forms.Form):
    question = forms.CharField(label='fquestion', max_length=100)

    def clean_question(self):
        question = self.cleaned_data['question']
        return question


class Top3Results(models.Model):
    def __str__(self):
        return self.result_text1,self.result_text2,self.result_text3

    result_text1 = models.CharField(max_length=2000)
    result_text2 = models.CharField(max_length=2000)
    result_text3 = models.CharField(max_length=2000)

class Top3Predition(models.Model) :
    def __str__(self):
        return self.result_texte1,self.result_texte2,self.result_texte3

    result_texte1 = models.CharField(max_length=2000)
    result_texte2 = models.CharField(max_length=2000)
    result_texte3 = models.CharField(max_length=2000)
