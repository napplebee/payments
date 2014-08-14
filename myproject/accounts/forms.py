from django import forms


class CreateAccountForm(forms.Form):
    name = forms.CharField(max_length=200, label="Name", initial="", error_messages={'required': 'Name is required field.'})
    view_order = forms.IntegerField(label="Order", initial="", error_messages={'required': 'Order is required field.'})
    is_default = forms.BooleanField(label="Set default")
    is_hidden = forms.BooleanField(label="Hide from the list")
