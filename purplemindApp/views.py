from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

from django.http import HttpResponse


class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'index.html', context=None)