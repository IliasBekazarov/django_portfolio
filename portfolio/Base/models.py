from django.db import models

# Create your models here.
class Contact(models.Model):
    name= models.CharField(max_length=40)
    email=models.EmailField(max_length=40)
    content=models.TextField(max_length=400)
    number=models.CharField(max_length=10)


    def __self__(self):
        return(self.name)
    
from django.db import models

class Page(models.Model):
    title = models.CharField(max_length=200)  # Баракчанын аты (мисалы, Home, About)
    content = models.TextField()  # Баракчанын мазмуну (HTML же текст)
    slug = models.SlugField(unique=True)  # URL үчүн уникалдуу аталыш (мисалы, home, about)
    created_at = models.DateTimeField(auto_now_add=True)  # Качан түзүлгөнү
    updated_at = models.DateTimeField(auto_now=True)  # Качан өзгөртүлгөнү

    def __str__(self):
        return self.title

from django.db import models

class AboutMe(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='about_images/')

    def __str__(self):
        return self.name

class Skill(models.Model):
    name = models.CharField(max_length=100)
    percentage = models.IntegerField()

    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    github_link = models.URLField()
    live_link = models.URLField()

    def __str__(self):
        return self.title

class ContactInfo(models.Model):
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.TextField()

    def __str__(self):
        return self.email