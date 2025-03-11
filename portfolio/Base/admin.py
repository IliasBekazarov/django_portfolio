from django.contrib import admin
from Base.models import Contact 
# Register your models here.
admin.site.register(Contact)

from django.contrib import admin
from .models import AboutMe, Skill, Project, ContactInfo

admin.site.register(AboutMe)
admin.site.register(Skill)
admin.site.register(Project)
admin.site.register(ContactInfo)

