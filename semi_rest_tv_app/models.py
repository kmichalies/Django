from django.db import models

class Network(models.Model):
    name = models.CharField(max_length=5, default='name')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    #shows = network from Show

class Show(models.Model):
    title = models.CharField(max_length=255)
    release_date = models.DateField()
    desc = models.TextField()
    network = models.ForeignKey(Network, related_name='shows', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
