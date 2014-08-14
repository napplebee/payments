from django.conf.urls import patterns, url
from myproject.accounts.controllers import AccountController

#from myproject.accounts import controllers
#account_controller = controllers.AccountController()

urlpatterns = patterns('',
    # url(r'^create$', account_controller.create, name="create"),
    url(r'^create$', AccountController.create, name="create"),
    url(r'^$', AccountController.index, name='index')
)
