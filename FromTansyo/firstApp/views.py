from django.shortcuts import render
from django.http import HttpResponse
from django.template.context_processors import csrf
# Create your views here.
def hello(request):
    return HttpResponse('こんにちは')

def welcome(request):
    name = '水原' #ここの名前を田中かほかの人の名前に変更します
    dictionary = {'name':name}
    return render(request,'name_if.html',dictionary)

def form_test(request):
    if request.method == 'POST':
        print(request.POST)
        return welcome2(request,request.POST['name'])

    elif request.method == 'GET':
        dictionary = {}
        dictionary.update(csrf(request))
        return render(request,'form.html',dictionary)

def welcome2(request,name):
    #name = '田中' ←コメントアウト
    dictionary = {'name':name}
    return render(request,'name_if.html',dictionary)
