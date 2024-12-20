from django.shortcuts import render,redirect
from.models import Gallery

# Create your views here.
def index(request):
    if request.method=='POST' and 'image' in request.FILES:
        myimage=request.FILES['image']
        obj=Gallery(feedimage=myimage)
        obj.save()
        return redirect('index')
    gallery_images=Gallery.objects.all()
    return render(request,"index.html",{"gallery_images":gallery_images})
