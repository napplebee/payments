import datetime
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import render

# Create your views here.
from myproject.accounts.models import Account
from myproject.settings import BASE_DIR, TEMPLATE_DIRS


def index(request):
    template = loader.get_template('base.html')
    context = RequestContext(request)
    return HttpResponse(template.render(context))


def create(request):
    return HttpResponse("hi there")