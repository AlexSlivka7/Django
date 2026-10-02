from django.shortcuts import render, HttpResponse

def ahoj(request):
    return HttpResponse("<h1>Ahoooooooj</h1>")

def o_mne(request):
    kontext = {
        'meno': 'Alex',
        'vek' : 17,
        'zaluby': ['hudba','hry','sport']
    }
    return render(request, 'ulohy/o_mne.html', kontext)

