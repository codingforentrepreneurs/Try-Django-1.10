from django.db import models

# Create your models here.

from .utils import code_generator, create_shortcode


class KirrURL(models.Model):
    url         = models.CharField(max_length=220, )
    shortcode   = models.CharField(max_length=15, unique=True, blank=True)
    updated     = models.DateTimeField(auto_now=True) #everytime the model is saved
    timestamp   = models.DateTimeField(auto_now_add=True) #when model was created
    #empty_datetime = models.DateTimeField(auto_now=False, auto_now_add=False)
    #shortcode = models.CharField(max_length=15, null=True) Empty in database is okay
    #shortcode = models.CharField(max_length=15, default='cfedefaultshortcode')

    def save(self, *args, **kwargs):
        if self.shortcode is None or self.shortcode == "":
            self.shortcode = create_shortcode(self)
        super(KirrURL, self).save(*args, **kwargs)

    # def my_save(self):
    #     self.save()

    def __str__(self):
        return str(self.url)

    def __unicode__(self):
        return str(self.url)



'''
python manage.py makemigrations
python manage.py migrate

python manage.py createsuperuser
'''