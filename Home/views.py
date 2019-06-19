from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'home.html')

def count(request):
    content=request.GET["text"]
    word_dict={}

    for word in content:
        if word not in word_dict:
            word_dict[word]=1
        else:
            word_dict[word]+=1
    sortedword = \
        sorted(word_dict.items(),key=lambda w:w[1],reverse=True)

    return render(request, 'count.html', dict(
        {'len':len(content),"content":content,"word_dict":sortedword}
    ))