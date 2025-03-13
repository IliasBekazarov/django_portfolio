from django.db import models

class Testimony(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='testimonies/')
    background_color = models.CharField(max_length=7, default="#ffffff")  # HEX түс коду


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = ' InfoOfSite'
        verbose_name_plural = ' InfoOfSite'
        
class Home(models.Model):
    menu_color = models.CharField(max_length=7, default="#ffffff")
    title = models.CharField(max_length=255)
    title_color = models.CharField(max_length=7, default="#ffffff")  # HEX түс коду
    name = models.CharField(max_length=255) 
    name_color = models.CharField(max_length=7, default="#ffffff")  # HEX түс коду
    description = models.CharField(max_length=255) 
    description_color = models.CharField(max_length=7, default="#ffffff")  # HEX түс коду
    image = models.ImageField(upload_to='home_images/', blank=True, null=True)  # Сүрөт
    logo = models.ImageField(upload_to='logo_images/', blank=True, null=True)  # Сүрөт
    resume_link = models.URLField(default="#about")  # Резюме шилтемеси
    hire_me_link = models.URLField(default="#contact")  # Байланыш шилтемеси
    background_color = models.CharField(max_length=7, default="#ffffff")  # HEX түс коду

    
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Home'
        verbose_name_plural = 'Home'



# Skills бөлүмү үчүн модел
class Skill(models.Model):
    name = models.CharField(max_length=100)
    name_color = models.CharField(max_length=7, default="#ffffff")  # HEX түс коду
    percentage = models.IntegerField()
    percentage_color = models.CharField(max_length=7, default="#ffffff")  # HEX түс коду
    image = models.ImageField(upload_to='skill_image/', blank=True, null=True)  # Сүрөт
   
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Skill'
        verbose_name_plural = 'Skill'

# Projects бөлүмү үчүн модел
class Project(models.Model):
    title = models.CharField(max_length=100)
    title_color = models.CharField(max_length=7, default="#ffffff")  # HEX түс коду
    description = models.TextField()
    description_color = models.CharField(max_length=7, default="#ffffff")
    github_link = models.URLField(blank=True, null=True)
    live_link = models.URLField(blank=True, null=True)
    image = models.ImageField(upload_to='project_images/', blank=True, null=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Project'


class Contact(models.Model):
    list_display = ('time_create')
    name = models.CharField(max_length=40)
    email = models.EmailField(max_length=40)
    content = models.TextField(max_length=400)
    number = models.CharField(max_length=10)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contact'

class AboutMe(models.Model):
    name = models.CharField(max_length=100)
    name_color = models.CharField(max_length=7, default="#ffffff")
    description = models.TextField()
    description_color = models.CharField(max_length=7, default="#ffffff")
    image = models.ImageField(upload_to='about_images/')
    hire_me_link = models.URLField(default="#contact")
    hire_me_link_color = models.CharField(max_length=7, default="#ffffff")
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'About Me'
        verbose_name_plural = 'About Me'