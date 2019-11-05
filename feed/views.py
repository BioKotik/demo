from django.shortcuts import render
from feed.models import Record
# Create your views here.

def all_records(request):
    records = Record.objects.all()
    return render(request, 'list.html', {'records': records})