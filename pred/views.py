from django.shortcuts import render, redirect
from pred.models import Anggota
from pred.forms import FormAnggota
from django.contrib import messages

def hapus_anggota(request, id_anggota):
	anggota = Anggota.objects.filter(id=id_anggota)
	anggota.delete()

	messages.success(request, "Data berhasil dihapus!")
	return redirect('anggota')

def ubah_anggota(request, id_anggota):
	anggota=Anggota.objects.get(id=id_anggota)
	template="ubah-anggota.html"
	if request.POST:
		form = FormAnggota(request.POST, instance=anggota)
		if form.is_valid():
			form.save()
			messages.success(request, "Data berhasil diubah!")
			return redirect('ubah_anggota', id_anggota=id_anggota)
	else:
		form=FormAnggota(instance=anggota)
		konteks = {
		'form' : form,
		'anggota' : anggota
		}
	return render(request, template, konteks)


def anggota(request):
	a =Anggota.objects.all()

	konteks = {
		'a' : a
	}
	return render(request, 'anggota.html', konteks)

def tambah_anggota(request):
	if request.POST:
		form = FormAnggota(request.POST)
		if form.is_valid():
			form.save()
			form = FormAnggota()
			pesan = "Data berhasil diupload!"
			konteks ={
				'form' : form,
				'pesan' : pesan
			}
			return render(request,'tambah-anggota.html', konteks)




	else:
		form = FormAnggota()

		konteks ={
			'form' : form
		}
		return render(request,'tambah-anggota.html', konteks)