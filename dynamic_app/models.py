from django.db import models

# Create your models here.
class AboutMe(models.Model):
    content = models.TextField()  # Content of the section (description)
    image = models.ImageField(upload_to='about_me_pics/', blank=True, null=True)  # Profile picture
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp when created
    updated_at = models.DateTimeField(auto_now=True)  # Timestamp when updated

    def __str__(self):
        return f"About Me (updated {self.updated_at})"

class Projet(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='project/')
    github_link = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title   

class Skill(models.Model):
    BEGINNER = 'beginner'
    INTERMEDIATE = 'intermediate'
    ADVANCED = 'advanced'

    PROFICIENCY_CHOICES = [
        (BEGINNER, 'Beginner'),
        (INTERMEDIATE, 'Intermediate'),
        (ADVANCED, 'Advanced'),
    ]
    
    name = models.CharField(max_length=100)  # Skill name
    proficiency = models.CharField(
        max_length=12,  # Increase max_length to accommodate the longest proficiency value
        choices=PROFICIENCY_CHOICES,
        default=BEGINNER,  # Default to beginner
    )  # Proficiency level (beginner, intermediate, advanced)
    description = models.TextField(blank=True, null=True)  # Optional description
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp when added

    def get_proficiency_class(self):
        if self.proficiency == self.BEGINNER:
            return 'beginner'  # Yellow
        elif self.proficiency == self.INTERMEDIATE:
            return 'intermediate'  # Green
        else:
            return 'advanced'  # Blue

    def __str__(self):
        return f"{self.name} ({self.proficiency})"