from django.db import models

# Create your models here.

from .utils import code_generator, create_shortcode

class ShortURLManager(models.Manager):
	"""docstring for ShortURLManager"""
	def all(self, *args, **kwargs):
		qs_main = super(ShortURLManager, self).all(*args, **kwargs)
		qs = qs_main.filter(active=True)
		return qs

def refresh_shortcodes(self):
	qs = ShortURL.objects.filter(id__gte=1)
	if items is not None and instance(items, int):
		qs = qs.order_by('id')[:items]
	new_codes = 0
	for q in qs:
		q.shortcode = create_shortcode(q)
		print(q.shortcode)
		q.save
		new_codes += 1
	return "New codes made: {i}".format(i=new_codes)

class ShortURL(models.Model):
	url = models.CharField(max_length=220, )
	shortcode = models.CharField(max_length=15, unique=True, blank=True)
	updated = models.DateTimeField(auto_now=True)
	timestamp = models.DateTimeField(auto_now_add=True)
	active = models.BooleanField(default=True)
	#empty_dayetime = models.DateTimeField(auto_now=False, auto_now_add=False)
	objects = ShortURLManager() #se usa objects.all() para invocar al metodo del manager

def save(self, *args, **kwargs):
	#print('sobreescritura de save')
	if self.shortcode is None or self.shortcode =="":
		self.shortcode = create_shortcode(self)
	super(ShortURL, self).save(*args, **kwargs)

	def __str__(self):
		return str(self.url)

	def __unicode__(self):
		return str(self.url)