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

    






def create(req):
    
    
    if req.method == "GET":
        return render(req,"create.html")
    
    elif req.method == 'POST':
        
       
        title = req.POST.get("title")
        year = req.POST.get("year")
        category = req.POST.get("genre")
        desc = req.POST.get("desc")
        img = req.FILES.get("image")
        rejissyor = req.POST.get("rej")
        time = req.POST.get("time")
        
        
        Movi.objects.create(title = title, year = int(year), category = category, desc = desc,image = img, rejissyor = rejissyor, time = time)
        
        
        
        
        return redirect("/")
    
        
    
    
    
def delete(req,id):
    
    if req.method == "POST":
        Movi.objects.get(id = id).delete()
        
        return redirect("/")
    if req.method == "GET":
        
        movie = Movi.objects.get(id = id)
        
        data = {
            "movie": movie
        }
        
        return render(req,'delete.html',context=data)
        


def update(req,id):
    if req.method == "GET":
        
        data = {
            "movie": Movi.objects.get(id = id)
        }
        return render(req, "update.html", context=data)
    
    if req.method == "POST":
        
        title =req.POST.get("title")
        year =req.POST.get("year")
        category = req.POST.get("category")
        desc = req.POST.get("desc")
        time = req.POST.get("time")
        
        image = req.FILES.get("image")
        
        
        movie = Movi.objects.get(id= id)
        
        if title:
            movie.title= title
        if year:
            movie.year = year
        if desc:
            movie.desc = desc
        if category:
            movie.category = category
        if image:
            movie.image = image
        if time:
            movie.time = time
        
        movie.save()
        
        return redirect("/")
        