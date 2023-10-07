from django.db import models
#from azure.storage.blob import BlobServiceClient, ContentSettings
from django.conf import settings
#from storages.backends.azure_storage import AzureStorage

# Create your models here.
"""class AzureBlobImageField(models.ImageField):
    def upload_to_azure(self, instance, filename):
        blob_service_client = BlobServiceClient(account_url=f"https://{settings.AZURE_ACCOUNT_NAME}.blob.core.windows.net", credential=settings.AZURE_ACCOUNT_KEY)
        container_client = blob_service_client.get_container_client(settings.AZURE_CONTAINER_MEDIA)
        
        blob_name = f"media/{filename}"
        blob_client = container_client.get_blob_client(blob_name)
        
        with self.storage.open(filename, 'rb') as file:
            blob_client.upload_blob(file, content_settings=ContentSettings(content_type=self.content_type))
        
        return blob_client.url

    def generate_filename(self, instance, filename):
        return self.upload_to_azure(instance, filename)
    
class MyAzureStorage(AzureStorage):
    location = 'media'

class identifier(models.Model):
    name=models.CharField(max_length=50)
    def __str__(self):
        return f'{self.name}'

class more_image(models.Model):
    title=models.CharField(max_length=50)
    picture=models.ImageField(upload_to='image', storage=MyAzureStorage())
    identifier=models.ForeignKey(identifier, on_delete=models.CASCADE, null=True, blank=False)
    def __str__(self):
        return f'{self.title}'

class project(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()
    identifier=models.ForeignKey(identifier, on_delete=models.CASCADE, null=True, blank=False)
    technology=models.CharField(max_length=50,blank=True, null=True)
    categoryapp=models.CharField(max_length=50, blank=True, null=True)
    categoryweb=models.CharField(max_length=50, blank=True, null=True)
    url=models.URLField(max_length=200)
    image=models.ImageField(upload_to='image', storage=MyAzureStorage())
    pictures=models.ManyToManyField(more_image)
    def __str__(self):
        return f'{self.title}'"""

class identifier(models.Model):
    name=models.CharField(max_length=50)
    def __str__(self):
        return f'{self.name}'

class more_image(models.Model):
    title=models.CharField(max_length=50)
    picture=models.ImageField(upload_to='image')
    identifier=models.ForeignKey(identifier, on_delete=models.CASCADE, null=True, blank=False)
    def __str__(self):
        return f'{self.title}'

class project(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()
    identifier=models.ForeignKey(identifier, on_delete=models.CASCADE, null=True, blank=False)
    technology=models.CharField(max_length=50,blank=True, null=True)
    categoryapp=models.CharField(max_length=50, blank=True, null=True)
    categoryweb=models.CharField(max_length=50, blank=True, null=True)
    url=models.URLField(max_length=200)
    image=models.ImageField(upload_to='image')
    pictures=models.ManyToManyField(more_image)
    def __str__(self):
        return f'{self.title}'
    
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

class dev_employment(models.Model):
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
    created_at= models.DateTimeField(auto_now_add=True)
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
    def __str__(self):
        return f'{self.name}'
    
class testimonial(models.Model):
    remark=models.TextField()
    picture=models.ImageField(upload_to='testimonial_images',blank=True, null=True)
    name=models.CharField(max_length=100)
    position=models.CharField(max_length=100, blank=True, null=True)
    organization=models.CharField(max_length=100, blank=True, null=True)
    def __str__(self):
        return f'{self.name}' 