from django import forms

class Filter(forms.Form):
    specie_degu = forms.BooleanField(label='Degu',required=False)
    specie_sapiens = forms.BooleanField(label='Sapiens',required=False)
    specie_nmr = forms.BooleanField(label='Naked Mole Rat',required=False)
    specie_rat = forms.BooleanField(label='Rat',required=False)