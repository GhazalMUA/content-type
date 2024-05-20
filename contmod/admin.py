from django.contrib import admin
from .models import Article,OnePart,Comment,Course
# Register your models here.

admin.site.register(Article)
admin.site.register(OnePart)
admin.site.register(Comment)
admin.site.register(Course)