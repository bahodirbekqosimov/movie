from django.shortcuts import render ,get_object_or_404, redirect
from .models import Movi




def home(req):
    
    movies = Movi.objects.all()
    
    data = {"movies":movies}
    
    return render(req,"index.html",context=data)


def detail(req,id):
    movi = Movi.objects.get(id = id)
    data = {"movi":movi}
    
    return render(req,'detail.html',context= data)

    


# def delete(req,id):



def create(req):
    
    
    if req.method == "GET":
        return render(req,"create.html")
    
    elif req.method == 'POST':
        
        # print(req.title)
        title = req.POST.get("title")
        year = req.POST.get("year")
        category = req.POST.get("genre")
        desc = req.POST.get("desc")
        img = req.POST.get("")
        
        
        
        
        return redirect("/")
    
        
    
    
    
    # Movi.objects.create(
    #     title = ""
    # )
    