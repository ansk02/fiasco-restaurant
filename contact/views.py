from django.shortcuts import render

# Create your views here.
def contacthome(request):
	return render(request, 'contact.html')