from django.db import models

# Create your models here.

from .utils import code_generator

class ShortURL(models.Model):
	url = models.CharField(max_length=220, )
	shortcode = models.CharField(max_length=15, unique=True, blank=True)
	updated = models.DateTimeField(auto_now=True)
	timestamp = models.DateTimeField(auto_now_add=True)
	#empty_dayetime = models.DateTimeField(auto_now=False, auto_now_add=False)

def save(self, *args, **kwargs):
	#print('sobreescritura de save')
	if self.shortcode is None or self.shortcode =="":
		self.shortcode = code_generator()
	super(ShortURL, self).save(*args, **kwargs)

	def __str__(self):
		return str(self.url)

	def __unicode__(self):
		return str(self.url)