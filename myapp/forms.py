from django import forms
from .models import Game


class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ['jmeno', 'vyvojari', 'popis', 'pocet_hodin', 'rok_vydani', 'zanry']