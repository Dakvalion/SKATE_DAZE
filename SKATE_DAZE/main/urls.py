from . import views
from django.urls import path
from SKATE_DAZE import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.SD),
    path('LogIn', views.LogIn),
    path('SignIn', views.SignIn),
    path('Catalog', views.Catalog),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
