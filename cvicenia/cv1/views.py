from django.shortcuts import render

def cv1_index(request):
    kontext = {
        "meno": "Alex Slivka",}
    return render(request, 'cv1/cv1_index.html', kontext)

def cv1_obchod(request):
    produkty = [
        {'nazov': 'Mlieko', 'cena': 1.43},
        {'nazov': 'Chleba', 'cena': 2.21},
        {'nazov': 'Maslo', 'cena': 3.28},
        {'nazov': 'Zemiaky', 'cena': 6.57}
    ] 
    max_cena = None
    max_cena_str = request.GET.get('max_cena', '')
   
    if max_cena_str:
            max_cena = float(max_cena_str)
            produkty = [produkt for produkt in produkty if produkt['cena'] <= max_cena]
    

    return render(request, 'cv1/cv1_obchod.html', {'produkty': produkty, 'max_cena': max_cena})

def cv1_body(request):
    priemer = None
    body = None
    maximum = None
    znamka = 5
    if request.method == 'POST':
        body = float(request.POST['body'])
        maximum = int(request.POST['maximum'])
        priemer = (body / maximum) * 100
        if priemer >= 90:
            znamka = "1"
        elif priemer >= 75:
            znamka = "2"
        elif priemer >= 50:
            znamka = "3"
        elif priemer >= 30:
            znamka = "4"
        else:
            znamka = "5"
    return render(request, 'cv1/cv1_body.html', {'body': body, 'maximum': maximum, 'priemer': priemer, 'znamka': znamka})
