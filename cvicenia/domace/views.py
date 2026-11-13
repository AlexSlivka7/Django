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

