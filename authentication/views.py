from django.shortcuts import render, redirect, reverse
from .forms import SignUpForm, UpdateUserForm
from django.contrib import messages
from application.models import Uzrasas, UzrasoKategorija
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required


def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registracija sėkminga! Dabar galite prisijungti.')
            return redirect(reverse('rodyti_mano_uzrasus'))
        messages.error(request, 'Neteisingai užpildyta forma!')
        return render(request, 'registration/sign_up.html', context={'form': form})
    else:
        form = SignUpForm()
    return render(request, 'registration/sign_up.html', context={'form': form})


@login_required
def user_account(request):
    uzrasu_skaicius = Uzrasas.objects.filter(uzraso_autorius=request.user.id).all().count()
    kategoriju_skaicius = UzrasoKategorija.objects.filter(kategorijos_autorius=request.user.id).all().count()
    if request.method == 'POST':
        form = UpdateUserForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Paskyra atnaujinta!')
            return redirect(reverse('user_account'))
        messages.warning(request, 'Neteisingai užpildyta forma!')
        return redirect(reverse('user_account'))
    else:
        form = UpdateUserForm(initial={
            'username': request.user.username,
            'email': request.user.email,
            'first_name': request.user.first_name,
            'last_name': request.user.last_name
        })
    return render(request, 'user_account.html', context={'form': form,
                                                         'uzrasu_skaicius': uzrasu_skaicius,
                                                         'kategoriju_skaicius': kategoriju_skaicius
                                                         })


@login_required
def user_logout(request):
    logout(request)
    messages.success(request, "Sėkmingai atsijungėte!")
    return redirect("rodyti_mano_uzrasus")
