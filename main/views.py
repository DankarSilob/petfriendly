# Create your views here.
from django.http import HttpResponse
from django.template import Context, loader
from django.http import Http404
from django.shortcuts import render, get_object_or_404

from main.models import Lugar
from main.models import CategoriaLugar

def index(request):	
	abs_uri = request.build_absolute_uri()
	lugares = Lugar.objects.all()
	template = loader.get_template('main/index.html')
	context = Context({
		'lugares' : lugares,
		'abs_uri':abs_uri
		})
	return HttpResponse(template.render(context))

def detail(request , id_lugar):
	markers = Lugar.objects.all()
	lugar = get_object_or_404(Lugar, pk=id_lugar)	
	categorias = CategoriaLugar.objects.all().filter(lugar=id_lugar)
	return render(request, 'main/detail.html', {'lugar': lugar, 'categorias':categorias})