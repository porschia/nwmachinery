from django.shortcuts import render
from django.http import HttpResponseRedirect
from website.ipware.ip import get_ip
from website.models import EmailCapture
from django.core.mail import send_mail

def ip_count(ip):
	p = EmailCapture.objects.filter(ip_address=ip)
	return p.count()
	
def home_page(request):
	return render(request, 'home.html')
	
def software(request):
	if request.method == 'POST':
		ip = get_ip(request)
		ip_number = ip_count(ip)
		form_name = request.POST['name']
		form_email = request.POST['email']
		form = EmailCapture.objects.create(name=form_name, email=form_email, ip_address=ip)
		
		send_mail('Software Interest', '%s has accessed the Inspect_it download page. The email entered was %s. This user has accessed the software %d times.' % (form_name, form_email, ip_number), 'tinadwilkerson@gmail.com', ['tinadwilkerson@gmail.com'])
		
		if ip_number > 5:
			return HttpResponseRedirect('/softwarepurchase')
		else:
			return HttpResponseRedirect('/softwaredownload')
		
	return render(request, 'software.html')
	
def contact(request):
		
	return render(request, 'contact.html')
	
def software_download(request):
	
	return render(request, 'SoftwareDownload.html')
	
def about(request):
	
	return render(request, 'About.html')
	
def inspections(request):

	return render(request, 'Inspections.html')
	
def software_purchase(request):
	
	return render(request, 'SoftwarePurchase.html')
