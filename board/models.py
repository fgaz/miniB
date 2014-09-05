from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=30, blank=True, null=True, )
    #author = models.CharField(max_length=30, blank=True, null=True, )
    date = models.DateTimeField(auto_now_add=True)
    content = models.TextField(max_length=1000)
    picURL = models.URLField(blank=True)

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['-id']