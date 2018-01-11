from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import Place


# Create your views here.
class Map(View):

    def get(self, request):
        opera = Place.objects.get(name='opera krakowska')
        context = {
            'name':opera.name,
            'description':'Opis',
            'lat':opera.lat,
            'long':opera.long}
        return render(request,'map/base.html',context)