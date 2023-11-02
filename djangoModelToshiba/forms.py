from django import forms
from djangoModelToshiba.models import Toshiba

class wanafunziform(forms.ModelForm):
    class Meta:
        model=Toshiba
        fields="__all__"