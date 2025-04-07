from django.db import models
#from cloudinary.models import CloudinaryField

# Create your models here.
class Service(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    
    
    def __str__(self):
        return self.title
    
    

class Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    skills = models.CharField(max_length=255)
    image_url = models.ImageField(upload_to='images/')
    #image = CloudinaryField('image', folder='projects')
    
    
    
    def __str__(self):
        return self.title



class ContactMessage(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return f"Message from {self.name}"
