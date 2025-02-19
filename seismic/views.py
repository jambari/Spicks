from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.template import loader
from .forms import WaveformUploadForm
from .models import SeismicWaveform
import os
import json
import numpy as np
import plotly.graph_objects as go
from django.shortcuts import render
from django.conf import settings
from .models import SeismicWaveform
from obspy import read
from .models import Station

def home(request):
    return render(request, 'home.html')  # Make sure you create this template

def upload_waveform(request):
    if request.method == "POST":
        form = WaveformUploadForm(request.POST, request.FILES)

        if form.is_valid():
            files = request.FILES.getlist('files')  # Get multiple files from the form

            # Save each file to the database
            for file in files:
                SeismicWaveform.objects.create(file=file)

            return redirect('waveform_list')  # Redirect after successful upload

    else:
        form = WaveformUploadForm()

    return render(request, 'upload.html', {'form': form})

#post the waveform
def waveform_list(request):
    waveforms = SeismicWaveform.objects.all()
    waveform_data = []

    for waveform in waveforms:
        file_path = os.path.join(settings.MEDIA_ROOT, str(waveform.file))

        try:
            # Read waveform file using ObsPy
            st = read(file_path)
            trace = st[0]  # Take the first trace (single-channel for now)

            # Convert data for Plotly
            time = np.linspace(0, trace.stats.npts * trace.stats.delta, trace.stats.npts)
            data_dict = {
                'id': waveform.id,
                'filename': waveform.file.name,
                'time': time.tolist(),
                'amplitude': trace.data.tolist(),
            }
            waveform_data.append(data_dict)

        except Exception as e:
            print(f"Error reading file {waveform.file.name}: {e}")

    return render(request, 'waveform_list.html', {'waveform_data': json.dumps(waveform_data)})


#this stations data for map
def stations_json(request):
    stations = Station.objects.all()
    features = []

    for station in stations:
        features.append({
            "type": "Feature",
            "properties": {
                "code": station.code,
                "network": station.network,
                "name": station.name,
                "location": station.name,  # Assuming name is from location
                "latitude": station.latitude,
                "longitude": station.longitude,
                "elevation": station.elevation,
            },
            "geometry": {
                "type": "Point",
                "coordinates": [station.longitude, station.latitude, station.elevation or 0]
            }
        })

    data = {
        "type": "FeatureCollection",
        "features": features
    }

    return JsonResponse(data)

#this is for station details
def station_details(request, code):
    # Get the station using the code from the URL
    station = get_object_or_404(Station, code=code)
    
    # Render a template with station details
    return render(request, 'station_details.html', {'station': station})