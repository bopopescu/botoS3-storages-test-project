from botoS3.forms import BotoS3Form
from botoS3.models import Resume
from django.shortcuts import render_to_response, get_object_or_404
from django.template import Context, RequestContext
from django.http import HttpResponse, HttpResponseRedirect

def load_botoS3_resume(request):

    form = BotoS3Form()
    if request.method == 'POST':
        form = BotoS3Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            rs = Resume.objects.all()
            return render_to_response('resume/success.html', context_instance=RequestContext(request,{'resume':rs}))
    
    return render_to_response('resume/form.html', context_instance=RequestContext(request,{'form':form}))

def success(request):
    rs = Resume.objects.all()
    return render_to_response('resume/success.html', context_instance=RequestContext(request,{'resume':rs}))