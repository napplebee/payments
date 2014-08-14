from django import forms


class CreateAccountForm(forms.Form):
    name = forms.CharField(max_length=200)
    created = forms.DateTimeField('date created')
    view_order = forms.IntegerField()
    is_default = forms.BooleanField()
    is_hidden = forms.BooleanField()
