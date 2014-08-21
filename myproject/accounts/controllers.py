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
        accounts = Account.objects.all()
        template = loader.get_template('accounts/index.html')
        context = RequestContext(request)
        return render(request, 'accounts/index.html', {
            'accs': accounts
        })

    @staticmethod
    def create(request):
        if request.method == 'POST':
            form = CreateAccountForm(request.POST)
            if form.is_valid():
                acc = Account(
                    name=form.cleaned_data["name"],
                    view_order=form.cleaned_data["view_order"],
                    is_default=form.cleaned_data["is_default"],
                    is_hidden=form.cleaned_data["is_hidden"],
                    created=datetime.datetime.now()
                )
                acc.save()
                return HttpResponseRedirect('/acc/')
        else:
            form = CreateAccountForm()

        action = 'Create'
        return render(request, 'accounts/create.html', {
            'f': form,
            'action': action
        })
