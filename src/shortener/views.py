from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views import View

from .models import KirrURL

# Create your views here.



def kirr_redirect_view(request, shortcode=None, *args, **kwargs): #function based view FBV
    obj = get_object_or_404(KirrURL, shortcode=shortcode)
    return HttpResponse("hello {sc}".format(sc=obj.url))



class KirrCBView(View): #class based view
    def get(self, request, shortcode=None, *args, **kwargs):
        obj = get_object_or_404(KirrURL, shortcode=shortcode)
        return HttpResponse("hello again {sc}".format(sc=shortcode))

    def post(self, request, *args, **kwargs):
        return HttpResponse()



'''

def kirr_redirect_view(request, shortcode=None, *args, **kwargs): #function based view FBV
    #print(request.user)
    #print(request.user.is_authenticated())\
    print('method is \n')
    print(request.method)
    #obj = KirrURL.objects.get(shortcode=shortcode)

    obj = get_object_or_404(KirrURL, shortcode=shortcode)
    #obj_url = obj.url
    # try:
    #     obj = KirrURL.objects.get(shortcode=shortcode)
    # except:
    #     obj = KirrURL.objects.all().first()


    # obj_url = None
    # qs = KirrURL.objects.filter(shortcode__iexact=shortcode.upper())
    # if qs.exists() and qs.count() == 1:
    #     obj = qs.first()
    #     obj_url = obj.url

    return HttpResponse("hello {sc}".format(sc=obj.url))

'''
