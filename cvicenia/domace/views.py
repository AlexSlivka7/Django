from django.shortcuts import render , HttpResponse

def domace(request):
    text = "Moje domáce úlohy"
    return render(request, 'domace/domace.html', {'text': text})