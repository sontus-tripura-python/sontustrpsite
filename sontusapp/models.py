from django.db import models
from django.urls import reverse
# Create your models here.
class AboutMe(models.Model):
    my_name = models.CharField(max_length=100, blank=True)
    About_photo = models.ImageField(upload_to='about_pic', blank=True, null=True)
    about_description = models.TextField(blank=True)

    def __str__(self):
        return self.my_name

class Contact(models.Model):
    serial_no = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    phone = models.CharField(max_length=11)
    email = models.CharField(max_length=20)
    message = models.TextField()
    status = models.CharField(max_length=20, default="New", choices=(("New", "New"), ("Read", "Read"), ("Closed", "Closed")))
    sentTime =models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class TimeLine(models.Model):
    title = models.CharField(max_length=100, blank=True)
    content_timeline = models.TextField(blank=True)

    def __str__(self):
        return self.title

class PortfolioCategory(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('portfolio_list_by_category', args = [self.slug])

class Portfolio(models.Model):
    category = models.ForeignKey(PortfolioCategory, null=True, blank=True, on_delete=models.CASCADE )
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)
    image = models.ImageField(upload_to='portfolio-img', blank=True)
    link = models.URLField(blank=True)
    description = models.TextField()

    def __str__(self):
        return self.name
