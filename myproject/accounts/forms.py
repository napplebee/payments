from django import forms


class CreateAccountForm(forms.Form):
    name = forms.CharField(max_length=200, label="Name")
    view_order = forms.IntegerField(label="Order")
    is_default = forms.BooleanField(label="Set default")
    is_hidden = forms.BooleanField(label="Hide from the list")
