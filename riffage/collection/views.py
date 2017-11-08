from django.http import *
from django.shortcuts import render, get_object_or_404, redirect
from .forms import RiffForm
from .models import Riff
from django.contrib import auth

def collection(request):
	riffs = Riff.objects.all()
	params = {}
	params['category'] = 'collections'
	return render(request, 'collection/collection.html',
		{ 'riffs' : riffs, 'params': params})

def riff_new(request):
	params = {}
	params['category'] = 'collections'
	if request.method == 'POST':
		form = RiffForm(request.POST, request.FILES)

		if form.is_valid():
			riff = form.save()

			return redirect('riff_detail', riff.pk)

	else:
		form = RiffForm()

	return render(request, 'collection/riff_new.html', {'form': form,'params': params})

def riff_detail(request, pk):
	params = {}
	params['category'] = 'collections'
	riff = get_object_or_404(Riff, pk=pk)
	return render(request, 'collection/riff_detail.html', {'riff': riff, 'params': params})

def riff_edit(request, pk):
	params = {}
	params['category'] = 'collections'
	riff = get_object_or_404(Riff, pk=pk)
	if request.method == "POST":
		form = RiffForm(request.POST, instance=riff, edit=True)
		if form.is_valid():
			riff = form.save()
			return redirect('riff_detail', riff.pk)
	else:
		form = RiffForm(instance=riff)
	
	return render(request, 'collection/riff_edit.html', {'form': form, 'params' : params})

def logout(request):
    auth.logout(request)
    return redirect('index')

def delete_riff(request, pk):
	riff = get_object_or_404(Riff, pk=pk)
	riff.delete()
	return redirect('collection')
