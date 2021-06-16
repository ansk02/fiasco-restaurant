from django.shortcuts import render

# Create your views here.

def recettehome(request):
	return render(request, 'recette.html')
