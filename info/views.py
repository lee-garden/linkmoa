from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def reference(request):
    return render(request, 'reference.html')

def downloadzip(request):
    file_path = "info/MoaMoa.zip"
    response = HttpResponse(open(file_path, 'rb'), content_type='application/zip')
    response["Content-Disposition"] = "attachment; filename=moamoa.zip"
    return response

def moaguide(request):
    return render(request, 'moaguide.html')