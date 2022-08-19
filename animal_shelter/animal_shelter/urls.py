"""animal_shelter URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from adoptions.views import AdoptionsViewSet, AnimalDetailView
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('api/adoptions',AdoptionsViewSet, 'adoptions')


urlpatterns = [
    path("admin/", admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html')),
    path('adopcje', TemplateView.as_view(template_name='adoptions.html'),name="adoptions"),
    path('adopcje/<int:pk>/', AnimalDetailView.as_view(), name='animal-detail'),
    path('adopcje', TemplateView.as_view(template_name='adoptions.html')),
    path('potrzeby/leki', TemplateView.as_view(template_name='meds.html')),
    path('potrzeby/leki', TemplateView.as_view(template_name='meds.html')),
    path('lapa/kontakt', TemplateView.as_view(template_name='contact.html'), name="contact"),
    path('lapa/o-nas', TemplateView.as_view(template_name='about.html'), name="about"),
    path('potrzeby/karma', TemplateView.as_view(template_name='food.html')),
    path('potrzeby/srodki-czystosci', TemplateView.as_view(template_name='cleaning.html')),

    *router.urls
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header  =  "Łapa Nysa"  
admin.site.site_title  =  "Łapa Nysa Panel Administratora"
admin.site.index_title  = "Administracja zwierzętami do adopcji" 