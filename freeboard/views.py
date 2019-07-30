from django.shortcuts import render

# Create your views here.
def freeboard(request):
    return render(request, 'freeboard.html')

def createpost(request):
    print('create')
    return redirect('freeboard')