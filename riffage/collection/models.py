from django.db import models

class Riff(models.Model):
	name = models.CharField(max_length=20)

	# This is the check-box for Private Visibility.
	# We default all riffs as Private (unchecked).
	priv_vis = models.BooleanField(default=True)

	KEY_CHOICES = [
		('', 'Select'),

		('Amaj', 'Amaj'),
		('Bmaj', 'Bmaj'),
		('Cmaj', 'Cmaj'),
		('Dmaj', 'Dmaj'),
		('Emaj', 'Emaj'),
		('Fmaj', 'Fmaj'),
		('Gmaj', 'Gmaj'),
		('Abmaj', 'Abmaj'),
		('Bbmaj', 'Bbmaj'),
		('Dbmaj', 'Dbmaj'),
		('Ebmaj', 'Ebmaj'),
		('Gbmaj', 'Gbmaj'),

		('Amin', 'Amin'),
		('Bmin', 'Bmin'),
		('Cmin', 'Cmin'),
		('Dmin', 'Dmin'),
		('Emin', 'Emin'),
		('Fmin', 'Fmin'),
		('Gmin', 'Gmin'),
		('Abmin', 'Abmin'),
		('Bbmin', 'Bbmin'),
		('Dbmin', 'Dbmin'),
		('Ebmin', 'Ebmin'),
		('Gbmin', 'Gbmin'),

		('Chromatic', 'Chromatic'),
	]

	riff_key = models.CharField(max_length=20, choices=KEY_CHOICES, default='Select')

	timesig_num = models.IntegerField(default=4)

	TIMESIG_DENOM_CHOICES = [
		(1, '1'),
		(2, '2'),
		(4, '4'),
		(8, '8'),
		(16, '16'),
		(32, '32'),
	]

	timesig_denom = models.IntegerField(choices=TIMESIG_DENOM_CHOICES, default=4)

	audio_file = models.FileField(upload_to='riffs/', blank=True, null=True)
	
	desc = models.TextField(max_length=200, default='', blank=True)

	tab = models.TextField(max_length=1000, default='G |----|\nD |----|\nA |----|\nE |----|\n')

	tags = models.CharField(max_length=50, default='')
