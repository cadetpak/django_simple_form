from django.shortcuts import render, redirect

def index(request):
	return render(request, 'surveys/index.html')

def process_form(request):
	if 'count' in request.session:
		request.session['count'] += 1
	else:
		request.session['count'] = 1

	request.session['info'] = {
		"Name": request.POST['name'],
		"Location": request.POST['location'],
		"Language": request.POST['language'],
		"Comment": request.POST['comment'],
	}
	return redirect('/result')

def result(request):
	return render(request, 'surveys/result.html')