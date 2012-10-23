from django.db import models

class Resume(models.Model):
    pdf = models.FileField(upload_to='pdfs', null=True, blank=True)
    photos = models.ImageField(upload_to='photos', null=True, blank=True)

    def __unicode__(self):
        return self.photos._get_url()
