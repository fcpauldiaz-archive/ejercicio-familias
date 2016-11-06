from django import forms
from families.models import Familia

class FamiliaForm(forms.ModelForm):
  class Meta:
    model = Familia
    fields = ('nombre', 'pais')