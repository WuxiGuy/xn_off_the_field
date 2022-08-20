from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.
def createNote(request):
    if request.method == 'POST': 
        title = request.POST.get('title') 
        note = request.POST.get('note') 
        Note.objects.create(
            title=title,
            note=note
        )
    return HttpResponse({"status": 'Success'}) 