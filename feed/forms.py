from django import forms


class SendEmailForm(forms.Form):
    my_email = forms.CharField(max_length=100)
    address = forms.EmailField()
    comment = forms.CharField(required=False, widget=forms.Textarea)
