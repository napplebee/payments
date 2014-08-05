<<<<<<< HEAD
import datetime
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import render

# Create your views here.
from tags.models import Tag


def index(request):
    tag = Tag()
    tag.name = "Common"
    tag.created = datetime.date.today()
    tags_list = [tag]
    template = loader.get_template('index.html')
    context = RequestContext(request, {
        'tags_list': tags_list,
    })
    return HttpResponse(template.render(context))
=======
from django.shortcuts import render

# Create your views here.
>>>>>>> 28b9de76079fa6991abd2d86254f27cd715ed890
