from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
#REQUEST -> RESPONSE
#REQUEST HANDLER
def ball_count(request):
    #pull data from db
    #transform data
    #send emails
    return HttpResponse('Hello World')