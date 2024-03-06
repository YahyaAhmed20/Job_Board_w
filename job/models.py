from django.db import models
from django.utils.text import slugify
from django_countries.fields import CountryField

# Create your models here.

JOB_TYPE=(
    ('Full Time','Full Time'),
    ('Part Time','Part Time'),
)

def image_upload(instance,filename):
    imagename,extention=filename.split(".")
    return 'jobs/%s.%s'%(instance.id,extention)
    

class Job(models.Model):
    title=models.CharField(max_length=100)
    job_tybe=models.CharField(max_length=15,choices=JOB_TYPE)
    country = models.CharField(max_length=200,  null=True, choices=CountryField().choices + [('', 'Select Country')])
 # Add the country field

    description=models.TextField(max_length=10000)
    published_at=models.DateTimeField(auto_now=True)
    Vacancy=models.IntegerField(default=1)
    salary=models.IntegerField(default=0)
    experince=models.IntegerField(default=1)
    image=models.ImageField(upload_to=image_upload)
    slug=models.SlugField(blank=True,null=True)
    
    def save(self,*args,**kwargs):
        self.slug = slugify(self.title)
        super(Job,self).save(*args,**kwargs)
     
    def __str__(self): 
        return self.title
    
    


    