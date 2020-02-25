from django.conf.urls import url,include
from django.contrib import admin
from kefiapp import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^kefiadmin/', admin.site.urls),
    url(r'',include("kefiapp.urls")),
    url(r'djrichtextfield/', include('djrichtextfield.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
