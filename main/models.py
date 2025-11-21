from django.db import models

class Movi(models.Model):
    title = models.CharField(max_length=150)    
    desc = models.TextField(max_length=5000)
    image = models.FileField(upload_to="images")
    year = models.IntegerField()
    category = models.CharField(max_length=150)
    time=  models.CharField()
    rejissyor = models.CharField( max_length=100)


    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    
        
    
    def __str__(self):
        return self.title
    
    

