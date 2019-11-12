from django import forms
from .models import Record

class SendEmailForm(forms.Form):
    my_email = forms.CharField(max_length=100)
    address = forms.EmailField()
    comment = forms.CharField(required=False, widget=forms.Textarea)


class RecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = ('title', 'body', 'state')

