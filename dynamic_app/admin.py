from django.contrib import admin
from .models import Projet, Skill, AboutMe

# Register your models here.
admin.site.register(AboutMe)
admin.site.register(Projet)
admin.site.register(Skill)