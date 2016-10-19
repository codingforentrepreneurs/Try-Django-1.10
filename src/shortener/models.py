from django.db import models

# Create your models here.

class KirrURL(models.Model):
    url = models.CharField(max_length=220, )
    shortcode = models.CharField(max_length=15, unique=True)
    #shortcode = models.CharField(max_length=15, null=True) Empty in database is okay
    #shortcode = models.CharField(max_length=15, default='cfedefaultshortcode')

    def __str__(self):
        return str(self.url)

    def __unicode__(self):
        return str(self.url)



'''
python manage.py makemigrations
python manage.py migrate

python manage.py createsuperuser
'''