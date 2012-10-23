from django.conf.urls.defaults import patterns, include, url
from django.views.generic.simple import direct_to_template
from botoS3.views import load_botoS3_resume


urlpatterns = patterns('botoS3.views',
    url(r'^$', 'load_botoS3_resume', name='load_botoS3_resume'),
    url(r'^success/', 'success', name='success'),
)