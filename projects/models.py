from django.db import models
import uuid



# Create your models here.
class Project(models.Model):
    title=models.CharField(max_length=200)
    description=models.TextField(blank=True,null=True)
    tags =models.ManyToManyField('Tag', blank=True)
    vote_total= models.IntegerField(default=0, blank=True, null=True)
    vote_ratio= models.IntegerField(default=0, blank=True, null=True)
    demo_link=models.TextField(blank=True,null=True)
    source_link=models.CharField(max_length=200,blank=True,null=True)
    created_time=models.DateTimeField(auto_now_add=True)
    id=models.UUIDField(default=uuid.uuid4,primary_key=True,editable=False)

    def __str__(self):
        return self.title

class Review(models.Model):
    VOTE_TYPE =(
        ('up','Up Vote'),
        ('down','Down Vote'),
    )
    #owner=
    project=models.ForeignKey(Project,on_delete=models.CASCADE)
    text=models.TextField(blank=True, null=True)
    value=models.CharField(max_length=200,choices=VOTE_TYPE)
    created_time= models.DateTimeField(auto_now_add=True)
    id=models.UUIDField(default=uuid.uuid4,primary_key=True,editable=False)


    def __str__(self):
        return self.value

class Tag(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    created_time= models.DateTimeField(auto_now_add=True)
    id=models.UUIDField(default=uuid.uuid4,primary_key=True,editable=False)


    def __str__(self):
        return self.name
