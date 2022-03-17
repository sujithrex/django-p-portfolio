from django.db import models

class all_blog(models.Model):
    title = models.CharField(max_length=100)
    postdate = models.DateField()
    body = models.TextField(max_length=2500)

    
    def  __str__(self):
        return self.title
