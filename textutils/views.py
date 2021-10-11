# I have created this File - Jayesh Patil

from django.http import HttpResponse
from django.shortcuts import render

# def index(request):
#     return HttpResponse('''<h1>Harry</h1> <a href="https://www.youtube.com/watch?v=AepgWsROO4k&list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9&index=7">DjangoCodeWithHarry"</a>''')
#
# def about(request):
#     return HttpResponse("Hello Jayesh patil")

# Code For Video 7

def index(request):
    return render(request,'index.html')
    # return HttpResponse("Home")

def analyze(request):
    # Get the text
    # print(request.GET.get('text','defult'))
    djtext = request.POST.get('text','defult')

    # Check Checkbox values
    removepunc = request.POST.get('check_removepunc','off')
    fullcaps = request.POST.get('fullcaps','off')
    newlineremover = request.POST.get('newlineremover','off')
    spaceremover = request.POST.get('spaceremover','off')
    charcount = request.POST.get('charcount','off')

    # Check which check box is on
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Remove Punctuations', 'analyzed_text': analyzed}
        # Analize the text
        djtext = analyzed
        # return render(request, 'analyze.html', params)

    if(fullcaps=="on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Remove Changed to upper case', 'analyzed_text': analyzed}
        # Analize the text
        djtext = analyzed
        # return render(request, 'analyze.html', params)

    if(newlineremover=="on"):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
        params = {'purpose': 'Remove New lines', 'analyzed_text': analyzed}
        # Analize the text
        djtext = analyzed
        # return render(request, 'analyze.html', params)

    if (spaceremover == "on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index + 1] == " "):
                analyzed = analyzed + char

        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        djtext = analyzed

    if (charcount == "on"):
        analyzed = ""
        count = 0
        for char in djtext:
            count = count + 1
        params = {'purpose': 'count character', 'analyzed_text': count}

    if (removepunc != "on" and newlineremover != "on" and spaceremover != "on" and fullcaps != "on"):
        return HttpResponse("please select any operation and try again")

    return render(request, 'analyze.html', params)


