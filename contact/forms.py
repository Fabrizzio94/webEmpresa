from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label="Nombre", required=True, widget=forms.TextInput(
        # diccionario de atributos
        attrs={'class': 'form-control','placeholder':'Nombre...'}
    ))
    email = forms.EmailField(label="Email", required=True, widget=forms.EmailInput(
        # diccionario de atributos
        attrs={'class': 'form-control','placeholder':'Email'}
    ))
    content = forms.CharField(label="Contenido",required=True, widget=forms.Textarea(
        # diccionario de atributos
        attrs={'class': 'form-control', 'rows': 3, 'placeholder':'Mensaje...'}
    ))