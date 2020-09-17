from django.shortcuts import render, redirect
from bs4 import BeautifulSoup
from urllib.request import urlopen
from django.http import HttpResponse
import bs4 as bs
import requests	
from .models import Word


def word_list(request):
    context = {}
    context["list"] = Word.objects.all()
    return render(request, 'bibleword/list.html', context)


def test(request):
    context = {}
    q = request.GET.get('q', None)
    items = ''
    if q == None or q ==  "":
        context = {}
    elif q is not None:
        post = Word.objects.filter(word=q.capitalize())
    return render(request, 'bibleword/home.html',context)
    
    
    
def home(request):
    context = {}
    q = request.GET.get('q', None)
    items = ''
    if q == None or q ==  "":
        context = {}
    elif q is not None:
        if Word.objects.filter(word = q).exists():
            word = Word.objects.filter(word__contains=q)
            print(word)
        else:
            word = q.lower()
            print(word)
            data = requests.get('https://biblespeak.org/'+q+'-pronunciation/')
            soup = BeautifulSoup(data.text, 'html.parser')
            word = soup.find('h1')
            word = word.text
            source = soup.find('source')
            audio = source['src']
            print(source)
            print(audio)
            if word == '404':
                redirect("search")
            else:
                word = word.capitalize()
                bible = Word.objects.all()
                if Word.objects.filter(word = word).exists():
                    word = Word.objects.filter(word__contains=q)
                else:    
                    word = Word.objects.create(word=word,audio_src=audio)
                    word.save()
                    word = Word.objects.filter(word__contains=q)
                print(word)
        context = {'word':word}
    return render(request, 'bibleword/home.html',context)
    
def search(request):
    q = request.GET.get('word', None)
    if q is not None:
        word = q.lower()
        print(word)
        data = requests.get('https://biblespeak.org/'+q+'-pronunciation/')
        soup = BeautifulSoup(data.text, 'html.parser')
        word = soup.find('h1')
        word = word.text
        source = soup.find('source')
        audio = source['src']
        print(source)
        print(audio)
        if word == '404':
            redirect("search")
        else:
            word = word.capitalize()
            bible = Word.objects.all()
            if Word.objects.filter(word = word).exists():
                pass
            else:    
                word = Word.objects.create(word=word,audio_src=audio)
                word.save()
                print(word)
    else:
        word = "Search for Word"
        audio = ""
        print(word)
    context = {'word':word, 'audio':audio}
    return render(request, 'word.html', context) 
    
    
def view_all(request):
    context = {}
    post = Word.objects.order_by('-date_created')
    context = {'post': post}
    return render(request, 'bibleword/home.html',context) 
    
def add(request):
    q = request.GET.get('q', None)
    items = ''
    if q != None:
        data = requests.get('https://biblespeak.org/'+ q +'-pronunciation/')
        soup = BeautifulSoup(data.text, 'html.parser')
        Name = soup.find_all('div', attrs={'class':'audiotop'})
        Name = soup.find('h1')
        Name = Name.text
        div = soup.find_all('div', attrs={'class':'audioleft'})
        audio_source = soup.find('source')
        audio = audio_source['src']
        print(audio)
        word = Word.objects.create(word=Name,audio_src=audio)
        word.save()
        context = {'word':post}
    elif q is not None:
        post = Word.objects.filter(word__contains=q)
        context = {'post': post}
    return render(request, 'bibleword/home.html',context)
 
        