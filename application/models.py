from django.db import models
from authentication.models import User


class UzrasoKategorija(models.Model):
    kategorija = models.CharField('Užrašo kategorija', max_length=50, null=False, blank=False)
    kategorijos_autorius = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.kategorija


class Uzrasas(models.Model):
    pavadinimas = models.CharField('Pavadinimas', max_length=50, null=False, blank=False)
    uzrasas = models.TextField('Užrašas', max_length=500, null=True, blank=True, help_text='Pagrindinis užrašo tekstas')
    uzraso_autorius = models.ForeignKey(User, on_delete=models.CASCADE)
    uzraso_kategorija = models.ForeignKey(UzrasoKategorija, on_delete=models.CASCADE)
    nuotrauka = models.ImageField('Nuotrauka', upload_to='uzrasu_nuotraukos', null=True, blank=True)
    data_sukurimo = models.DateTimeField('Data', auto_now_add=True)

    def __str__(self):
        return self.uzrasas
