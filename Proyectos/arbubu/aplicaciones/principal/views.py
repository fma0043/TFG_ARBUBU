from django.shortcuts import render

from django.http import HttpResponse

from django.template import RequestContext

from django.views.generic import(
    ListView,
    TemplateView,
    CreateView,
)

class IndexView(TemplateView):

    template_name = "principal/index.html"
