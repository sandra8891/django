from django.shortcuts import render,redirect
from.models import *
def index(request):
    if request.POST:
        name2=request.POST.get("name")
        date2=request.POST.get("date")
        course2=request.POST.get("course")
        obj1=Listitime(name1=name2,date1=date2,course1=course2)
        obj1.save()
        return redirect(index)
    data=Listitime.objects.all()
    return render(request,"index.html",{"feeds":data})
    



# Create your views here.
