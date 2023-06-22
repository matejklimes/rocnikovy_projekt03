from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Genre(models.Model):
    nazev = models.CharField(max_length=20, verbose_name='Název žánru', help_text='Zadejte název žánru')
    popis = models.TextField(blank=True, verbose_name='Popis žánru', help_text='Vložte popis žánru')

    class Meta:
        ordering = ['nazev']
        verbose_name = 'Žánr'
        verbose_name_plural = 'Žánry'

    def __str__(self):
        return f'{self.nazev}'


class Developer(models.Model):
    jmeno = models.CharField(max_length=100, verbose_name='Jméno vývojáře', help_text='Zadejte jméno vývojáře', error_messages={'blank': 'Jméno vývojáře je povinný údaj'})
    stat = models.CharField(blank=True, null=True, max_length=50, verbose_name='Stát')

    class Meta:
        ordering = ['jmeno']
        verbose_name = 'Vývojář'
        verbose_name_plural = 'Vývojář'

    def __str__(self):
        return f'{self.jmeno}'


class Game(models.Model):
    jmeno = models.CharField(max_length=100, verbose_name='Jméno hry', help_text='Zadejte jméno hry', error_messages={'blank': 'Jméno hry musí být vyplněn'})
    vyvojari = models.ManyToManyField(Developer, verbose_name='Vývojáři')
    popis = models.TextField(blank=True, verbose_name='Popis hry', help_text='Vložte popis hry')
    pocet_hodin = models.PositiveIntegerField(blank=True, null=True, validators=[MaxValueValidator(500)], verbose_name='Délka hry', help_text='Zadejte délku hry v hodinách (max. 500)')
    rok_vydani = models.PositiveIntegerField(blank=True, null=True, validators=[MinValueValidator(1950), MaxValueValidator(2100)], verbose_name='Rok vydání', help_text='Zadejte rok vydání (1950 - 2100)')
    zanry = models.ManyToManyField(Genre, verbose_name='Žánry')

    class Meta:
        ordering = ['jmeno']
        verbose_name = 'Hra'
        verbose_name_plural = 'Hry'

    def __str__(self):
        return f'{self.jmeno} ({self.rok_vydani})'



class Rating(models.Model):
    text = models.TextField(verbose_name="Text recenze", help_text="Zadej text recenze")
    hra = models.ForeignKey('Game', on_delete=models.PROTECT, verbose_name='Hra')
    recenzent = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Recenzent')
    HODNOCENI = (
        (0, ''),
        (1, '*'),
        (2, '**'),
        (3, '***'),
        (4, '****'),
        (5, '*****')
    )
    hodnoceni = models.PositiveSmallIntegerField(choices=HODNOCENI, verbose_name='Hodnocení', default=3)
    cas = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['hra', 'recenzent']
        verbose_name = 'Recenze'
        verbose_name_plural = 'Recenze'

    def __str__(self):
        return f'Recenze hry {self.hra} od {self.recenzent} ({self.cas.year})'
