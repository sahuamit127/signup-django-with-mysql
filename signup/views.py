from django.shortcuts import render
from django.http import HttpResponse
from signup.forms import formadddata
def index(request):
    form=formadddata()
    if request.method =="POST":
        form = formadddata(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'form.html', {'tk':'thanks'})
    context= {'form': form }
    return render(request, 'index.html', context)
