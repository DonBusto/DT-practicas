from django import forms
from .models import Activity


class ActivityForm (forms.Form):
    cnae = forms.IntegerField()#widget=forms.IntegerField(max_value=1000,widget=forms.IntegerField({'class' : 'form-control'})))
    peso = forms.FloatField()#(widget=forms.IntegerField(max_value=1000,widget=forms.FloatField({'class' : 'form-control'}))))

class NewActivityForm(forms.ModelForm):
    class Meta:
        model = Activity
        fields = ['cnae', 'peso']
