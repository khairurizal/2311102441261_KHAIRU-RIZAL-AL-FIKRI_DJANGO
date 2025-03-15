from django.contrib import admin
from django.urls import path

## ini untuk menampilkan gambar yang sdh di upload 
from django.conf import settings
from django.conf.urls.static import static

from webrzl.views import home, about
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('about', about, name="about"),
]

## ini untuk menampilkan gambar yang sdh di upload 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)