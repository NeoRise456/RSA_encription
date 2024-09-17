from django import forms

class TextoForm(forms.Form):
    texto = forms.CharField(widget=forms.Textarea)