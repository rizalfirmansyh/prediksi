from django.db import models

class Channel_yt(models.Model):
	Channel = models.CharField(max_length=30)
	Keterangan = models.TextField()

	def __str__(self):
		return self.Channel

class Anggota(models.Model):
	Nama_Asli = models.CharField(max_length=30)
	Julukan = models.CharField(max_length=30)
	Motor = models.CharField(max_length=30)
	Channel_yt_id = models.ForeignKey(Channel_yt, on_delete=models.CASCADE, null=True)

	def __str__(self):
		return self.Nama_Asli 