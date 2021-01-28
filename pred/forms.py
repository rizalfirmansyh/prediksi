from django.forms import ModelForm
from django import forms
from pred.models import Anggota

class FormAnggota(ModelForm):
	class Meta:
		model = Anggota
		fields ='__all__'

		widgets = {
		'Nama_Asli' : forms.TextInput({'class':'form-control'}), 
		'Julukan' : forms.TextInput({'class':'form-control'}),
		'Motor' : forms.TextInput({'class':'form-control'}),
		'Channel_yt_id' : forms.Select({'class':'form-control'}),
		}