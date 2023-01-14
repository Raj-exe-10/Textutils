#I created this file -Harsh
import os
from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return render(request,'index.html')

def index2(request):
    return render(request,'index2.html')
def analyze2(request):
    #get Text
    djtext = request.POST.get('text','default')

    #Checking the textbox value
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    spaceremover = request.POST.get('spaceremover', 'off')
    charcounter = request.POST.get('charcounter', 'off')

    #defining a default string for result
    analyzed=""



    #defining the punctuation function if it is selected
    if removepunc =='on':
        # defining the punctuation it need to remove
        punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for i in djtext:
            if i not in punc:
                analyzed = analyzed+i
        # print(analyzed)
        params = {'purpose': "Removing Punctuations", 'analyzed_text': analyzed}

        #Analyze the text
        return render(request, 'analyze2.html', params)

    # defining the Uppercase function if it is selected
    if fullcaps=='on':
        analyzed=""
        for i in djtext:
            analyzed = analyzed+i.upper()
        # print(analyzed)
        params = {'purpose': "Changing characters to uppercase", 'analyzed_text': analyzed}
        return render(request, 'analyze2.html', params)

    #Defining new line function
    if(newlineremover=='on'):
        analyzed = ""
        for i in djtext:
            if i != '\n' and i !='\r':
                analyzed = analyzed + i
        # print(analyzed)
        params = {'purpose': "Removing the new lines", 'analyzed_text': analyzed}
        return render(request, 'analyze2.html', params)

    # Defining space remover function
    if (spaceremover == 'on'):
        analyzed = ""
        # Enumerate function returns the present index value
        for index,i in enumerate(djtext):
            if not(djtext[index]==" " and djtext[index+1]==" "):
                analyzed = analyzed + i
        # print(analyzed)
        params = {'purpose': "Removing the extra spaces", 'analyzed_text': analyzed}
        return render(request, 'analyze2.html', params)

    # Defining the char counter function
    if (charcounter == 'on'):
        analyzed = 0
        for i in djtext:
            if not(i==" " or i=="\n"):
                analyzed = analyzed + 1
        # print(analyzed)
        params = {'purpose': "Counting the total charactters", 'analyzed_text': analyzed}
        return render(request, 'analyze2.html', params)
    if (removepunc != "on" and newlineremover != "on" and spaceremover != "on" and fullcaps != "on"):
        return HttpResponse("please select any operation and try again")




