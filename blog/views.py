from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
posts=[
    {
        'title':'blog posts',
        'author':'Dawit Mekonnen',
        'date_posted':'sep 2 2021',
        'content':'programing languge'
    },
     {
        'title':'tplf is terrerist',
        'author':'nahom bezin ',
        'date_posted':'sep 2 2021',
        'content':'as we all know that tplf started a war in november 3 20201 and still now '
    }
]
def home(request):
    context={'posts':posts}
    return render(request,'blog/home.html',context)

def about(request):
    return render(request,'blog/about.html',{'title':'title'})