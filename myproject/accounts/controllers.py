import datetime
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.shortcuts import render

# Create your views here.
from myproject.accounts.forms import CreateAccountForm
from myproject.accounts.models import Account
from myproject.settings import BASE_DIR, TEMPLATE_DIRS


class AccountController:
    @staticmethod
    def index(request):
        template = loader.get_template('accounts/index.html')
        context = RequestContext(request)
        return HttpResponse(template.render(context))

    @staticmethod
    def create(request):
        if request.method == 'POST': # If the form has been submitted...
            # ContactForm was defined in the previous section
            form = CreateAccountForm(request.POST) # A form bound to the POST data
            if form.is_valid(): # All validation rules pass
                # Process the data in form.cleaned_data
                # ...
                return HttpResponseRedirect('/acc/') # Redirect after POST
        else:
            form = CreateAccountForm() # An unbound form

        return render(request, 'accounts/create.html', {
            'form': form,
        })
