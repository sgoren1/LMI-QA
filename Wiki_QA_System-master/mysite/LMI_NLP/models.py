import datetime
from django.db import models
from django.utils import timezone


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
