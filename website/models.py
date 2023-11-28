from django.db import models
# Create your models here.




      
class product(models.Model):
    name= models.CharField(max_length=50)
    description = models.TextField()
    Date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to= 'product_images',null=True, blank=True)
   

    def __str__(self):
        return self.name



class Resume(models.Model):
    resume = models.ImageField(upload_to= 'images',null=True, blank=True)





class Contact(models.Model):
    name = models.CharField(max_length=122)
    desc = models.TextField()
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=20, default=0)
    date = models.DateField()

    def __str__(self): 
        return self.name
