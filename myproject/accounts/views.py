import datetime
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import render

# Create your views here.
from myproject.accounts.models import Account


def index(request):
    template = loader.get_template('index.html')
    context = RequestContext(request)
    return HttpResponse(template.render(context))