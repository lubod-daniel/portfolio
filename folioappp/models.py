from django.db import models

# Create your models here.

class project(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()
    technology=models.CharField(max_length=50)
    category=models.CharField(max_length=50)
    url=models.URLField(max_length=200)
    image=models.ImageField(upload_to='images')
    def __str__(self):
        return f'{self.title}'
    
class image(models.Model):
    img=models.ImageField(upload_to='images', blank=True, null=True)
    img1=models.ImageField(upload_to='images', blank=True, null=True)
    img2=models.ImageField(upload_to='images', blank=True, null=True)
    img3=models.ImageField(upload_to='images',blank=True, null=True)
    def __str__(self):
        return f'{self.img}'

class responsibility(models.Model):
    duty=models.CharField(max_length=200)
    def __str__(self):
        return f'{self.duty}'
    

class employment(models.Model):
    designation=models.CharField(max_length=100)
    start_date=models.CharField(max_length=50, blank=True, null=True)
    end_date=models.CharField(max_length=50, blank=True, null=True)
    employer=models.CharField(max_length=100, blank=True, null=True)
    employer_address=models.CharField(max_length=200, null=True)
    responsibility=models.ManyToManyField(responsibility)
    def __str__(self):
        return f'{self.designation}'

class qualification(models.Model):
    bag=models.CharField(max_length=100)
    year=models.CharField(max_length=50, blank=True, null=True)
    institution=models.CharField(max_length=100)
    about=models.CharField(max_length=500)
    def __str__(self):
        return f'{self.bag}'
    
class skill(models.Model):
    skill_acquired=models.CharField(max_length=200)
    def __str__(self):
        return f'{self.skill_acquired}'

class professional_course(models.Model):
    bag=models.CharField(max_length=200)
    year=models.CharField(max_length=100, blank=True, null=True)
    institution=models.CharField(max_length=200)
    skill=models.ManyToManyField(skill)
    def __str__(self):
        return f'{self.bag}'

class VisitorMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    
