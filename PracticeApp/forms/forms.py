from django import forms

SIGNOS = (
    ('Aries','Aries'),
    ('Tauro','Tauro'),
    ('Géminis','Géminis'),
    ('Cáncer','Cáncer'),
    ('Leo','Leo'),
    ('Virgo','Virgo'),
    ('Libra','Libra'),
    ('Escorpio','Escorpio'),
    ('Sagitario','Sagitario'),
    ('Capricornio','Capricornio'),
    ('Acuario','Acuario'),
    ('Piscis','Piscis'))

class FormularioX(forms.Form):
    nombre=forms.CharField()
    signo=forms.ChoiceField(choices=SIGNOS)
