from django.shortcuts import render

# Create your views here.
def skils(request):
	context = {'skill': 'active'}
	return render (request,'edu/skill.html',context)