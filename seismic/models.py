from django.db import models

# Create your models here.
class SeismicWaveform(models.Model):
    file = models.FileField(upload_to='waveforms/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.file.name
    

class Station(models.Model):
    code = models.CharField(max_length=10, unique=True)
    network = models.CharField(max_length=10)
    name = models.CharField(max_length=100, null=True, blank=True)
    latitude = models.FloatField()
    longitude = models.FloatField()
    elevation = models.FloatField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return f"{self.code} ({self.network})"

class Event(models.Model):
    origin_time = models.DateTimeField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    depth = models.FloatField()
    magnitude = models.FloatField()
    event_type = models.CharField(max_length=20, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Event {self.id} - M{self.magnitude}"

class Arrival(models.Model):
    station = models.ForeignKey(Station, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    arrival_time = models.DateTimeField()
    amp = models.FloatField(null=True, blank=True)
    per = models.FloatField(null=True, blank=True)
    res = models.FloatField(null=True, blank=True)
    dist = models.FloatField(null=True, blank=True)
    az = models.FloatField(null=True, blank=True)
    mb = models.FloatField(null=True, blank=True)
    ML = models.FloatField(null=True, blank=True)
    mBbig = models.FloatField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Arrival at {self.station.code} for Event {self.event.id}"