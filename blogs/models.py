from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
from django_quill.fields import QuillField


class Blogs(models.Model):
    title = models.CharField(max_length=255)
    short_description = models.CharField(max_length=765)
    featured_image = models.ImageField(upload_to='media/blogs/image')
    author = models.CharField(max_length=255)
    is_atHome = models.BooleanField(default=False)
    content = QuillField()
    date = models.DateField(auto_created=True)
    slug = models.SlugField(blank=True,null=True)

    meta_title = models.CharField(max_length=255,null=True,blank=True,help_text="if leave it will take from title ")
    meta_description = models.CharField(max_length=255,null=True,blank=True)
    meta_keywords = models.TextField(null=True,blank=True,help_text="use comma( , ) for separation")


    def __str__(self):
        return self.title + " - " + str(self.date)

    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        if self.meta_title == None:

            self.meta_title = self.title

        if self.meta_description == None:

            self.meta_description = self.short_description
        return super(Blogs,self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("details", kwargs={"slug": self.slug})


class Stories(models.Model):
    name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    content = models.CharField(max_length=565)
    isfemale = models.BooleanField(default=False)

    def __str__(self):
        return self.name + " - " + str(self.position)
    

class Getmails(models.Model):
    email = models.EmailField(max_length=255)

    def __str__(self):
        return self.email
    
