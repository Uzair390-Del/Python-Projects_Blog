from django.contrib import admin
from .models import Post,Course, Material

admin.site.register(Post)
class MaterialInline(admin.TabularInline):
    model = Material
    extra = 1  # Number of extra material fields

class CourseAdmin(admin.ModelAdmin):
    inlines = [MaterialInline]

admin.site.register(Course, CourseAdmin)


# Register your models here.
