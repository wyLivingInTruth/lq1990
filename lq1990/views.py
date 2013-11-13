#encoding=utf-8

from django.http import response
from django.shortcuts import render
from .forms import UploadFileForm

def home(request):
	return render(request, 'home.html', {})

def upload(request):
	#这里如何使用request的method属性
	if request.method == 'GET':
		return render(request, 'upload.html', {})
	elif request.method == 'POST':
		f = request.FILES['file']
		return render(request, 'upload_sucess.html', {})
		
def articles(request):
	return render(request, 'articles.html', {})
