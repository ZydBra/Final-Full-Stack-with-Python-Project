from django.shortcuts import render, redirect, get_object_or_404
from .models import Uzrasas, UzrasoKategorija
from .forms import KategorijosForma, UzrasoForma
from django.contrib import messages
from django.db.models import Q
from itertools import chain


def prideti_kategorija(request):
    uzrasu_skaicius = Uzrasas.objects.filter(uzraso_autorius=request.user.id).all().count()
    kategoriju_skaicius = UzrasoKategorija.objects.filter(kategorijos_autorius=request.user.id).all().count()
    kategorijos_uzrasuose = UzrasoKategorija.objects.filter(kategorijos_autorius=request.user.id).all().values()
    if request.method == 'POST':
        form = KategorijosForma(request.POST)
        if form.is_valid():
            kategorija = form.save(commit=False)
            kategorija.kategorijos_autorius = request.user
            kategorija.save()
            messages.success(request, 'Kategorija pridėta!')
            return redirect('rodyti_mano_kategorijas')
        messages.warning(request, 'Neteisingai užpildyti laukai!')
        return render(request, 'prideti_kategorija.html', context={'form': form})
    else:
        form = KategorijosForma()
    return render(request, 'prideti_kategorija.html', context={'form': form,
                                                               'kategorijos_uzrasuose': kategorijos_uzrasuose,
                                                               'uzrasu_skaicius': uzrasu_skaicius,
                                                               'kategoriju_skaicius': kategoriju_skaicius
                                                               })


def prideti_uzrasa(request):
    uzrasu_skaicius = Uzrasas.objects.filter(uzraso_autorius=request.user.id).all().count()
    kategoriju_skaicius = UzrasoKategorija.objects.filter(kategorijos_autorius=request.user.id).all().count()
    kategorijos_uzrasuose = UzrasoKategorija.objects.filter(kategorijos_autorius=request.user.id).all().values()
    if request.method == 'POST':
        form = UzrasoForma(request.POST, request.FILES, kategorijos_autorius=request.user.id)
        if form.is_valid():
            uzrasas = form.save(commit=False)
            uzrasas.uzraso_autorius = request.user
            uzrasas.save()
            messages.success(request, 'Užrašas sukurtas!')
            return redirect('rodyti_mano_uzrasus')
        messages.warning(request, 'Neteisingai užpildyti laukai!')
        return render(request, 'prideti_uzrasa.html', context={'form': form})
    else:
        form = UzrasoForma(kategorijos_autorius=request.user.id)
    return render(request, 'prideti_uzrasa.html', context={'form': form,
                                                           'kategorijos_uzrasuose': kategorijos_uzrasuose,
                                                           'uzrasu_skaicius': uzrasu_skaicius,
                                                           'kategoriju_skaicius': kategoriju_skaicius})


def rodyti_mano_uzrasus(request):
    uzrasai = Uzrasas.objects.filter(uzraso_autorius=request.user.id).all()
    kategorijos_uzrasuose = UzrasoKategorija.objects.filter(kategorijos_autorius=request.user.id).all().values()
    uzrasu_skaicius = Uzrasas.objects.filter(uzraso_autorius=request.user.id).all().count()
    kategoriju_skaicius = UzrasoKategorija.objects.filter(kategorijos_autorius=request.user.id).all().count()
    return render(request, 'mano_uzrasai.html', context={'uzrasai': uzrasai,
                                                         'kategorijos_uzrasuose': kategorijos_uzrasuose,
                                                         'uzrasu_skaicius': uzrasu_skaicius,
                                                         'kategoriju_skaicius': kategoriju_skaicius})


def rodyti_mano_kategorijas(request):
    kategorijos = UzrasoKategorija.objects.filter(kategorijos_autorius=request.user.id).all()
    uzrasu_skaicius = Uzrasas.objects.filter(uzraso_autorius=request.user.id).all().count()
    kategoriju_skaicius = UzrasoKategorija.objects.filter(kategorijos_autorius=request.user.id).all().count()
    kategorijos_uzrasuose = UzrasoKategorija.objects.filter(kategorijos_autorius=request.user.id).all().values()
    return render(request, 'mano_kategorijos.html', context={'kategorijos': kategorijos,
                                                             'kategorijos_uzrasuose': kategorijos_uzrasuose,
                                                             'uzrasu_skaicius': uzrasu_skaicius,
                                                             'kategoriju_skaicius': kategoriju_skaicius})


def kategorija(request, kategorija_id):
    paviene_kategorija = Uzrasas.objects.filter(uzraso_kategorija=kategorija_id)
    kategorijos_pavadinimas = UzrasoKategorija.objects.get(id=kategorija_id)
    kategorijos_uzrasuose = UzrasoKategorija.objects.filter(kategorijos_autorius=request.user.id).all().values()
    uzrasu_skaicius = Uzrasas.objects.filter(uzraso_autorius=request.user.id).all().count()
    kategoriju_skaicius = UzrasoKategorija.objects.filter(kategorijos_autorius=request.user.id).all().count()
    return render(request, 'kategorija.html', context={'paviene_kategorija': paviene_kategorija,
                                                       'kategorijos_pavadinimas': kategorijos_pavadinimas,
                                                       'kategorijos_uzrasuose': kategorijos_uzrasuose,
                                                       'uzrasu_skaicius': uzrasu_skaicius,
                                                       'kategoriju_skaicius': kategoriju_skaicius})


def uzrasas(request, uzrasas_id):
    kategorijos_uzrasuose = UzrasoKategorija.objects.filter(kategorijos_autorius=request.user.id).all().values()
    pavienis_uzrasas = Uzrasas.objects.filter(id=uzrasas_id)
    uzraso_pavadinimas = Uzrasas.objects.get(id=uzrasas_id)
    return render(request, 'uzrasas.html', context={'pavienis_uzrasas': pavienis_uzrasas,
                                                    'uzrasas': uzraso_pavadinimas,
                                                    'kategorijos_uzrasuose': kategorijos_uzrasuose})


def kategoriju_paieska(request):
    kategorijos_uzrasuose = UzrasoKategorija.objects.filter(kategorijos_autorius=request.user.id).all().values()
    query = request.GET.get('query')
    kategorijos = UzrasoKategorija.objects.filter(kategorijos_autorius=request.user.id).all()
    paieskos_rezultatas = kategorijos.filter(Q(kategorija__icontains=query))
    return render(request, 'ketegoriju_paieska.html', {'kategorijos': paieskos_rezultatas,
                                                       'query': query,
                                                       'kategorijos_uzrasuose': kategorijos_uzrasuose})


def uzrasu_paieska(request):
    kategorijos_uzrasuose = UzrasoKategorija.objects.filter(kategorijos_autorius=request.user.id).all().values()
    query = request.GET.get('query')
    uzrasai = Uzrasas.objects.filter(uzraso_autorius=request.user.id).all()
    kategorijos = UzrasoKategorija.objects.filter(kategorijos_autorius=request.user.id).all()
    paieska_uzrasuose = uzrasai.filter(Q(uzrasas__icontains=query) | Q(pavadinimas__icontains=query))
    paieska_kategorijose = kategorijos.filter(Q(kategorija__icontains=query))
    paieskos_rezultatas = list(chain(paieska_uzrasuose, paieska_kategorijose))
    return render(request, 'uzrasu_paieska.html', {'uzrasai': paieskos_rezultatas,
                                                   'query': query,
                                                   'kategorijos_uzrasuose': kategorijos_uzrasuose})


def atnaujinti_mano_kategorija(request, kategorija_id):
    kategorijos_uzrasuose = UzrasoKategorija.objects.filter(kategorijos_autorius=request.user.id).all().values()
    kategorijos_modelis = UzrasoKategorija.objects.get(id=kategorija_id)
    if request.method == 'POST':
        form = KategorijosForma(request.POST, instance=kategorijos_modelis)
        if form.is_valid():
            form.save()
            messages.success(request, 'Kategorija atnaujinta!')
            return redirect('rodyti_mano_kategorijas')
        messages.warning(request, 'Neteisingai užpildyti laukai!')
        return render(request, 'prideti_kategorija.html', context={'form': form})
    else:
        form = KategorijosForma(initial={'kategorija': kategorijos_modelis.kategorija})
    return render(request, 'prideti_kategorija.html', context={'form': form,
                                                               'kategorijos_uzrasuose': kategorijos_uzrasuose})


def istrinti_kategorija(request, kategorija_id):
    kategorijos_uzrasuose = UzrasoKategorija.objects.filter(kategorijos_autorius=request.user.id).all().values()
    kategorijos_modelis = UzrasoKategorija.objects.get(id=kategorija_id)
    if request.method == 'POST':
        kategorijos_modelis.delete()
        messages.success(request, 'Kategorija ištrinta!')
        return redirect('rodyti_mano_kategorijas')
    return render(request, 'istrinimo_patvirtinimas.html', context={'form': kategorijos_modelis,
                                                                    'kategorijos_uzrasuose': kategorijos_uzrasuose})


def keisti_uzrasa(request, uzrasas_id):
    kategorijos_uzrasuose = UzrasoKategorija.objects.filter(kategorijos_autorius=request.user.id).all().values()
    keiciamas_uzrasas = Uzrasas.objects.get(id=uzrasas_id)
    if request.method == 'POST':
        form = UzrasoForma(request.POST, request.FILES, instance=keiciamas_uzrasas,
                           kategorijos_autorius=request.user.id)
        if form.is_valid():
            form.save()
            messages.success(request, 'Užrašas atnaujintas!')
            return redirect('rodyti_mano_uzrasus')
        messages.warning(request, 'Neteisingai užpildyti laukai!')
        return render(request, 'prideti_uzrasa.html', context={'form': form})
    else:
        form = UzrasoForma(initial={
            'pavadinimas': keiciamas_uzrasas.pavadinimas,
            'uzrasas': keiciamas_uzrasas.uzrasas,
            'uzraso_kategorija': keiciamas_uzrasas.uzraso_kategorija,
            'nuotrauka': keiciamas_uzrasas.nuotrauka,
        }, kategorijos_autorius=request.user.id)
    return render(request, 'prideti_uzrasa.html', context={'form': form,
                                                           'kategorijos_uzrasuose': kategorijos_uzrasuose})


def istrinti_uzrasa(request, uzrasas_id):
    kategorijos_uzrasuose = UzrasoKategorija.objects.filter(kategorijos_autorius=request.user.id).all().values()
    trinamas_uzrasas = Uzrasas.objects.get(id=uzrasas_id)
    if request.method == 'POST':
        trinamas_uzrasas.delete()
        messages.success(request, 'Užrašas ištrintas!')
        return redirect('rodyti_mano_uzrasus')
    return render(request, 'istrinimo_patvirtinimas.html', context={'form': trinamas_uzrasas,
                                                                    'kategorijos_uzrasuose': kategorijos_uzrasuose})
