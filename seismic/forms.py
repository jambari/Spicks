from django import forms
from .models import SeismicWaveform

# Custom widget to allow multiple file selection
class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True

# Custom field to handle multiple files
class MultipleFileField(forms.FileField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("widget", MultipleFileInput())
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        # Handle the case where multiple files are uploaded
        if isinstance(data, (list, tuple)):
            # Apply the clean method of the FileField class for each file in the list
            return [forms.FileField().clean(d, initial) for d in data]
        return super().clean(data, initial)

# Custom form for file upload
class WaveformUploadForm(forms.Form):
    files = MultipleFileField()  # Use the custom MultipleFileField
