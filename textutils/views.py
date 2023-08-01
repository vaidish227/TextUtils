# i have  created this file
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')



def analyze(request):
    #get the text 
    djtext = request.POST.get('text','default')

    #check checkbox values
    removepunc = request.POST.get('removepunc','off')
    fullcaps = request.POST.get('fullcaps','off')
    newlineremover = request.POST.get('newlineremover','off')
    extraspaceremover = request.POST.get('extraspaceremover','off')
    wordcount = request.POST.get('wordcount','off')
    
    #check which checkbox is on 
    if removepunc == "on":
        punctuations = '''!()-{}[];,:<>?/""'.@#$%^&*_~`"'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations','analyzed_text': analyzed}
        return render(request, 'analyze.html',params)
    

    elif(fullcaps=="on"):
        analyzed= ""
        for char in djtext:
            analyzed = analyzed + char.upper()
            params = {'purpose': 'Change to upper case','analyzed_text': analyzed}
        return render(request, 'analyze.html',params)
    
    elif(newlineremover=="on"):
        analyzed=""
        for char in djtext:
            if char !="\n":
                analyzed = analyzed + char
            params = {'purpose': 'Removed new lines','analyzed_text': analyzed}
        return render(request, 'analyze.html',params)
    
    
    elif(extraspaceremover=="on"):
        analyzed=""
        for index, char in enumerate (djtext):
            if not (djtext[index] ==" " and djtext[index+1] == " "):
                analyzed = analyzed + char
            params = {'purpose': 'Removed spaces','analyzed_text': analyzed}
        return render(request, 'analyze.html',params)
    
    elif(wordcount=="on"):
        analyzed=""
        #djtxt=len(djtext.split())
        for char in djtext:
                djtxt=len(djtext.split())
                analyzed = str(djtxt)
        params = {'purpose': 'Word count','analyzed_text': analyzed}
        return render(request, 'analyze.html',params)
    
    else:
        return HttpResponse("Error")
