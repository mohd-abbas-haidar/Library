# from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import Books
# Create your views here.
def index(request):
    return render (request, 'index.html')


def library(request):
    all_book=Books.objects.all()
    books_list = [x for x in list(all_book)]
    return render (request,'library.html',{'book':books_list})