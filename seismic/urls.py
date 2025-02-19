from django.urls import path
from .views import upload_waveform
from .views import waveform_list
from .views import stations_json
from .views import station_details

urlpatterns = [
    path('upload/', upload_waveform, name='upload_waveform'),
    path('waveforms/', waveform_list, name='waveform_list'),
    path('stations/', stations_json, name='stations_json'),
    path('stations/<str:code>/', station_details, name='station_details'),
]

