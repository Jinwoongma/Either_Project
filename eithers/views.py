from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.contrib import messages
import requests

from .models import Question, Answer
from .form import QuestionForm, AnswerForm

def index(request):
    questions = Question.objects.all().order_by('-id')
    return render(request, 'eithers/index.html', {
        'questions': questions,
    })


def create(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save()
            return redirect('eithers:index')
    else:
        form = QuestionForm()
    context = {
        'form': form
    }
    return render(request, 'eithers/form.html', context)


def vote(request, question_pk):
    if request.method == "POST":
        question = get_object_or_404(Question, pk=question_pk)
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.question = question
            answer.save()
            messages.success(request, '댓글이 등록되었습니다.')
        else:
            messages.warning(request, '잘못된 댓글 형식입니다.')
        return redirect('eithers:vote', question_pk)
    else:
        question = Question.objects.get(pk=question_pk)
        GIPHY_API = 'b0GIlipiKq6qMKrOdSVxAAKRgjYK1Otn'
        url1 = f'http://api.giphy.com/v1/gifs/search?api_key={GIPHY_API}&q={question.selection1}&limit=1&lang=ko'
        url2 = f'http://api.giphy.com/v1/gifs/search?api_key={GIPHY_API}&q={question.selection2}&limit=1&lang=ko'
        data1 = requests.get(url1).json()
        data2 = requests.get(url2).json()
        print(data2)
        if data1.get('data') != []:
            image1 = data1.get('data')[0].get('images').get('original').get('url')
        else:
            image1 = "https://gph.is/XGFQMo"
        if data2.get('data') != []:
            image2 = data2.get('data')[0].get('images').get('original').get('url')
        else:
            image2 = "https://gph.is/XGFQMo"
        answers = question.answer_set.all()

        if len(answers) !=0:
            pick1 = question.answer_set.filter(pick=0).count()
            pick1_per = str(round(pick1/len(answers)*100))+'%'
            pick2 = question.answer_set.filter(pick=1).count()
            pick2_per = str(round(pick2/len(answers)*100))+'%'
        else:
            pick1_per ='0'
            pick2_per ='0'

        context = {
            'question' : question,
            'answers' : answers,
            'pick1_per': pick1_per,
            'pick2_per' : pick2_per,
            'image1' : image1,
            'image2' : image2,
            }
        return render(request, 'eithers/vote.html', context)