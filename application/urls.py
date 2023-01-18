from django.urls import path
from . import views

urlpatterns = [
    path('', views.rodyti_mano_uzrasus, name='rodyti_mano_uzrasus'),
    path('prideti_kategorija/', views.prideti_kategorija, name='prideti_kategorija'),
    path('prideti_uzrasa/', views.prideti_uzrasa, name='prideti_uzrasa'),
    path('mano_uzrasai/', views.rodyti_mano_uzrasus, name='rodyti_mano_uzrasus'),
    path('mano_kategorijos/', views.rodyti_mano_kategorijas, name='rodyti_mano_kategorijas'),
    path('kategoriju_paieska/', views.kategoriju_paieska, name='kategoriju_paieska'),
    path('uzrasu_paieska/', views.uzrasu_paieska, name='uzrasu_paieska'),
    path('kategorija/<int:kategorija_id>', views.kategorija, name='kategorija'),
    path('uzrasas/<int:uzrasas_id>', views.uzrasas, name='uzrasas'),
    path('atnaujinti_mano_kategorija/<int:kategorija_id>/', views.atnaujinti_mano_kategorija,
         name='atnaujinti_mano_kategorija'),
    path('istrinti_kategorija/<int:kategorija_id>/', views.istrinti_kategorija, name='istrinti_kategorija'),
    path('keisti_uzrasa/<int:uzrasas_id>/', views.keisti_uzrasa, name='keisti_uzrasa'),
    path('istrinti_uzrasa/<int:uzrasas_id>/', views.istrinti_uzrasa, name='istrinti_uzrasa'),
]
