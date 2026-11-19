from django.shortcuts import render, HttpResponse


def domace(request):
    text = "Moje domáce úlohy"
    return render(request, 'domace/domace.html', {'text': text})


def du2_(request):
    kontext = {
        "meno": "Alex",
        "trieda": "3.AT",
        "vek": 17,
        "zaluby": ["prax", "matematika", "fyzika"]
    }
    return render(request, 'domace/vizitka.html', kontext)


def du3_teplota(request):
    vysledok = None
    if request.method == 'POST':
        teplota = float(request.POST['teplota'])
        smer = request.POST['smer']
        if smer == 'c_na_f':
            prepocet = round(teplota * 9 / 5 + 32, 1)
            vysledok = f"{prepocet} °F"
        elif smer == 'f_na_c':
            prepocet = round((teplota - 32) * 5 / 9, 1)
            vysledok = f"{prepocet} °C"
    return render(request, 'domace/du3_teplota.html', {'vysledok': vysledok})

