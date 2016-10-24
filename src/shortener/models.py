from django.conf import settings
from django.db import models
from django.utils.encoding import smart_text
#from django.core.urlresolvers import reverse
from django_hosts.resolvers import reverse
# Create your models here.
from .utils import code_generator, create_shortcode
from .validators import validate_url, validate_dot_com

SHORTCODE_MAX = getattr(settings, "SHORTCODE_MAX", 15)


class KirrURLManager(models.Manager):
    def all(self, *args, **kwargs):
        qs_main = super(KirrURLManager, self).all(*args, **kwargs)
        qs = qs_main.filter(active=True)
        return qs

    def refresh_shortcodes(self, items=None):
        qs = KirrURL.objects.filter(id__gte=1)
        if items is not None and isinstance(items, int):
            qs = qs.order_by('-id')[:items]
        new_codes = 0
        for q in qs:
            q.shortcode = create_shortcode(q)
            print(q.id)
            q.save()
            new_codes += 1
        return "New codes made: {i}".format(i=new_codes)


class KirrURL(models.Model):
    url         = models.CharField(max_length=220, validators=[validate_url, validate_dot_com])
    shortcode   = models.CharField(max_length=SHORTCODE_MAX, unique=True, blank=True)
    updated     = models.DateTimeField(auto_now=True) #everytime the model is saved
    timestamp   = models.DateTimeField(auto_now_add=True) #when model was created
    active      = models.BooleanField(default=True)

    objects = KirrURLManager()
 

    def save(self, *args, **kwargs):
        if self.shortcode is None or self.shortcode == "":
            self.shortcode = create_shortcode(self)
        if not "http" in self.url:
            self.url = "http://" + self.url
        super(KirrURL, self).save(*args, **kwargs)

    def __str__(self):
        '''
        Added 'smart_text' function for rendering issues within
        Admin console. This code was after series completed.
        Updated: October 24 2016
        '''
        return smart_text(self.url)

    def __unicode__(self):
        '''
        Added 'smart_text' function for rendering issues within
        Admin console. This code was after series completed.
        Updated: October 24 2016
        '''
        return smart_text(self.url)

    def get_short_url(self):
        url_path = reverse("scode", kwargs={'shortcode': self.shortcode}, host='www', scheme='http')
        return url_path









