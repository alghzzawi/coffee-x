from django.db import models
from accounts.models import CustomUser
from django.urls import reverse
# Create your models here.

class Coffee(models.Model):
    title=models.CharField(max_length=255,null=False,blank=True)
    purchaser=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    price=models.CharField(max_length=255,null=False,blank=False)
    reviewer=models.TextField()
    img_url=models.TextField(default='no image')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('coffee_detail',args=[self.id])