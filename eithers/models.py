from django.db import models

# Create your models here.
class Question(models.Model):
    title = models.CharField(max_length=50)
    selection1 = models.CharField(max_length=50)
    selection2 = models.CharField(max_length=50)

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    pick = models.IntegerField()
    comment = models.TextField()