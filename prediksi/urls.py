from django.contrib import admin
from django.urls import path
from pred.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('anggota/', anggota, name = 'anggota'),
    path('tambah-anggota/', tambah_anggota, name ='tambah_anggota'),
    path('anggota/ubah/<int:id_anggota>', ubah_anggota, name='ubah_anggota'),
    path('anggota/hapus/<int:id_anggota>', hapus_anggota, name='hapus_anggota'),

]
