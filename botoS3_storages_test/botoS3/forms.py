from django.forms import ModelForm
from botoS3.models import Resume

class BotoS3Form(ModelForm):
    class Meta:
        model=Resume