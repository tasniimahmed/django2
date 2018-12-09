from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted= models.DateTimeField(default=timezone.now)
    #Foreign key for many to one relationship, y3ni kza user aw post 3andhom nafs el author
    #on delete 3shan han3ml eh fel post lw el user etmsa7? hanmsa7 el post bardo. bs lw mas7t el post msh hymsa7 el user tab3n
    author = models.ForeignKey(User,on_delete= models.CASCADE)

    #3shan nbayn eh el gwa el post lma nktb fel shell post.obj.all
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
