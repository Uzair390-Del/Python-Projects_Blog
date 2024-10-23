from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# import markdown

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    # author = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # created_at = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title
class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
class Material(models.Model):
    course = models.ForeignKey(Course, related_name='materials', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    file = models.FileField(upload_to='course_materials/')
    
    # Optional: Adding Markdown support (if you want to store HTML version)
    # html_content = models.TextField(blank=True, null=True)

    # def save(self, *args, **kwargs):
    #     # Automatically convert Markdown to HTML (if the file is .md)
    #     if self.file.url.endswith('.md'):
    #         with open(self.file.path, 'r', encoding='utf-8') as f:
    #             text = f.read()
    #             self.html_content = markdown.markdown(text)
    #     super().save(*args, **kwargs)

# class Material(models.Model):
#     course = models.ForeignKey(Course, related_name='materials', on_delete=models.CASCADE)
#     title = models.CharField(max_length=200)
#     file = models.FileField(upload_to='course_materials/')
# Create your models here.
