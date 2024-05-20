from django.shortcuts import render
from django.views import View
from .models import Article , Comment 

# Create your views here.

class Home(View):
    def get(self,request):
        maghale_made_nazar= Article.objects.first()
        comment_morede_nazar=Comment.objects.create(user=request.user , body='great!!!!' , content_object=maghale_made_nazar)
        return render (request , 'home.html' , {'comment_morede_nazar':comment_morede_nazar}) 