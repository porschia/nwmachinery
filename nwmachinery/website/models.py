from django.db import models

class EmailCapture(models.Model):
	name = models.TextField()
	email = models.EmailField()
	date_submitted = models.DateTimeField(auto_now_add=True)
	ip_address = models.GenericIPAddressField()
	
	def __str__(self):
		return self.ip_address
