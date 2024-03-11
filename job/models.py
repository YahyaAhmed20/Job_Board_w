from django.db import models
from django.utils.text import slugify
from django_countries.fields import CountryField
from django.contrib.auth.models import User

# Create your models here.

JOB_TYPE=(
    ('Full Time','Full Time'),
    ('Part Time','Part Time'),
)

def image_upload(instance,filename):
    imagename,extention=filename.split(".")
    return 'jobs/%s.%s'%(instance.id,extention)
    

class Job(models.Model):
    owner=models.ForeignKey(User,related_name='job_owner',on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    job_tybe=models.CharField(max_length=15,choices=JOB_TYPE)
    country = models.CharField(max_length=200,null=True, choices=CountryField().choices + [('', 'Select Country')])
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
# متنساش لما user يبقه عامل signin ميظهرلوش غير apply

# متنساش الترجمه 
class Apply(models.Model):
    job=models.ForeignKey(Job, related_name='apply_job', on_delete=models.CASCADE)
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=100)
    website=models.URLField(null=True,blank=True)
    cv=models.FileField(upload_to='apply/',)
    cover_letter=models.TextField(max_length=500)
    created_at=models.DateTimeField(auto_now=True)
    
     
    
    def __str__(self):
        return self.name
    


    