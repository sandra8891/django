from django.shortcuts import render,redirect

# Create your views here.
def index(request):
    if request.POST:
        title=request.POST.get("data")
        print(title)
        return redirect("about")
    return render(request,"index.html")
def about(request):
    return render(request,"about.html")
