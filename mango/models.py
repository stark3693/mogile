from django.db import models
class post(models.Model):
    image=models.ImageField(upload_to="cadd/images" , default="")
    image2=models.ImageField(upload_to="cadd/images" , default="")
    image3=models.ImageField(upload_to="cadd/images" , default="")
    im=models.ImageField(upload_to="cadd/images" , default="")
# Create your models here.
