from django.http import HttpResponse
from django.shortcuts import render
import operator
import string


def home(request):
    return render(request, 'home.html')


def count(request):
    fulltext = request.GET["fulltext"]
    wordlist = fulltext.split(' ')
    words = len(wordlist)
    worddict = {}
    for word in wordlist:
        word = word.translate(str.maketrans('', '', string.punctuation))
        if word.lower() in worddict:
            worddict[word.lower()] += 1;
        else:
            worddict[word.lower()] = 1;

    sorteddict = sorted(worddict.items(), key=operator.itemgetter(1), reverse=True)
    return render(request, 'count.html', {'fulltext': fulltext, 'count': words, 'worddict': sorteddict})


def about(request):
    return render(request, 'about.html')
