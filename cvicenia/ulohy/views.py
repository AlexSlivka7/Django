from django.shortcuts import render , HttpResponse
from datetime import date

def ahoj(request):
    return HttpResponse("Ahoj svet")

def o_mne(request):
    kontext = {
        "meno": "Alex",
        "vek": 17,
        "zaluby":["skola", "matematika", "hokej"]
    }
    return render(request, 'ulohy/o_mne.html', kontext)

def rozvrh(request):
    hodiny = [
        {"cislo" :1, "predmet": "Programovanie",},
        {"cislo" :2, "predmet": "Programovanie",},
        {"cislo" :3, "predmet": "Programovanie",},
        {"cislo" :4, "predmet": "Anglicky jazyk",},
        {"cislo" :5, "predmet": "Prax",},
        {"cislo" :6, "predmet": "Prax",},
        {"cislo" :7, "predmet": "Telesná výchova",},
    ]
    return render(request, 'ulohy/rozvrh.html', {'den': "Piatok", 'hodiny': hodiny})

def pozdrav(request):
    meno = request.GET.get('meno', '')  #.get najde a vrati hodnotu prvku s indexom(klucom) meno ak ho nenajde vlozi prazdny string
    return render(request, 'ulohy/pozdrav.html', {'meno': meno})

def sucet(request):
    vysledok = None
    if request.method == 'POST':
        a = int(request.POST['a'])
        b = int(request.POST['b'])
        vysledok = a + b
    return render(request, 'ulohy/sucet.html', {'vysledok': vysledok})

def kalkulacka(request):
    vysledok = None
    if request.method == 'POST':
        a = int(request.POST['a'])
        b = int(request.POST['b'])
        operacia = request.POST['operacia']
        if operacia == '+':
            vysledok = a + b
        elif operacia == '-':
            vysledok = a - b
        elif operacia == '*':
            vysledok = a * b
        elif operacia == '/':
            vysledok = a / b
    return render(request, 'ulohy/kalkulacka.html', {'vysledok': vysledok})

def obdlznik(request):
    obsah = None
    obvod = None
    if request.method == 'POST':
        a = float(request.POST['a'])
        b = float(request.POST['b'])
        obsah = round(a * b, 2)
        obvod = round(2 * (a + b), 2)
    return render(request, 'ulohy/obdlznik.html', {'obsah': obsah, 'obvod': obvod})

def vek(request):
    vek = None
    if request.method == 'POST':
        rok_narodenia = int(request.POST['rok_narodenia'])
        aktualny_rok = date.today().year
        vek = aktualny_rok - rok_narodenia
    return render(request, 'ulohy/vek.html', {'vek': vek})