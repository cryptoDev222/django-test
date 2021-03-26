from django.shortcuts import render
from django.http import HttpResponse

def detail(request, question_id):
    return HttpResponse("You are looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

# Create your views here.
