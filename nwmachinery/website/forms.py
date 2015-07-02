from django import forms

#class SoftwareForm(ModelForm):
#	class Meta:
#		model = EmailCapture
#		fields = ['name', 'email]

class SoftwareForm(forms.Form):
	name = forms.CharField(label='Your Name', max_length=100)
	
	email = forms.EmailField(label='Your Email')
