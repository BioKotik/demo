from django.urls import path
from . import views

app_name = 'feed'

urlpatterns = [
    path('', views.all_records, name='list_view'),
]