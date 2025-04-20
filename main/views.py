from django.shortcuts import render,get_object_or_404

def index(request):
	return render(request,'main/index.html')

def about(request):
	return render(request, 'main/about.html')

def issues(request):
	return render(request, 'main/issues_addressed.html')

def solution(request):
	return render(request, 'main/solution.html')

def terms(request):
	return render(request, 'main/terms.html')

def prospective(request):
	return render(request, 'main/prospective.html')		
