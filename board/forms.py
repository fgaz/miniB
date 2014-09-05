from django import forms


class PostForm(forms.Form):
    title = forms.CharField(required=False, label="Titolo")
    content = forms.CharField(widget=forms.Textarea, label="Contenuto (richiesto)")
    picURL = forms.URLField(required=False, label="Indirizzo dell'immagine")