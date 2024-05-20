#




from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericRelation , GenericForeignKey


class Article(models.Model):
    title=models.CharField(max_length=80)
    body=models.TextField()
    comment=GenericRelation('Comment')
    

    
class OnePart(models.Model):
    title=models.CharField(max_length=80)
    body=models.TextField(max_length=80)
    comment=GenericRelation('Comment')
    
class Course(models.Model):
    title=models.CharField(max_length=80)
    length=models.PositiveBigIntegerField()        
    comment=GenericRelation('Comment')
    
class Comment(models.Model):       #bayad tavajo dashte bashim ke content_type va object_id vaseye admin panel hastan va vaghti mikhaym code benevism masalan quest benevisim too view ya too shell code benevisim dg niazi nist be in dota tooye modele comment meghdar dehi konim on moghe faghat az morede akhar k content_object hastesh estefade mikonim.
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    body=models.CharField(max_length=80)
    
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey("content_type", "object_id")

    