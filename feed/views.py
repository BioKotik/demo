from django.shortcuts import render, get_object_or_404
from feed.models import Record
from feed.forms import SendEmailForm
from django.core.mail import send_mail
from django.views.generic import ListView

# Create your views here.


def all_records(request):
    a = 10
    records = Record.objects.all()
    return render(request, 'list.html', {'records': records})


class RecordListView(ListView):
    queryset = Record.objects.all()
    context_object_name = 'records'
    template_name = 'list.html'


def detailed_view(request, yy, mm, dd, slug):
    record = get_object_or_404(Record,
                               slug=slug,
                               pub__year=yy,
                               pub__month=mm,
                               pub__day=dd)
    return render(request, 'detailed.html', {"record": record})


def send_email(request, record_id):
    obj = get_object_or_404(Record, id=record_id)
    sent = False
    if request.method == "POST":
        form = SendEmailForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            obj_url = request.build_absolute_uri(obj.get_absolute_url())
            subject = "Owner {} recommends you reading {}".format(cd['my_email'], obj.title)
            message = "Read {} at {} \n\nAdded comment: {}".format(obj.title,
                                                                   obj_url,
                                                                   cd['comment'])
            send_mail(subject, message, 'admin@myblog.com', [cd['address']])
            sent = True
    else:
        form = SendEmailForm()
    return render(request, 'send.html', {'record': obj,
                                         'form': form,
                                         'sent': sent},
                  )