from django.db import models
from django.utils import timezone
from datetime import timedelta


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def recently_published(self):
        now = timezone.now()
        return now - timedelta(days=1) <= self.pub_date <= now

    recently_published.admin_order_field = 'pub_date'
    recently_published.boolean = True
    recently_published.short_description = 'Published recently?'


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
