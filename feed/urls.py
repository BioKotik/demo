from django.urls import path
from . import views

app_name = 'feed'

urlpatterns = [
    path('', views.all_records, name='list_view'),
    path('<int:yy>/<int:mm>/<int:dd>/<slug:slug>',
         views.detailed_view,
         name='detailed_view'),
    path('<int:record_id>/send/', views.send_email, name='send_email'),
]