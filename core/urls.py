from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # For the user authentications(BUILT-IN)
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls')),
    
    path('admin/', admin.site.urls),
    path('jobs/', include('job.urls')),
    path('contact-us/', include('contact.urls')),
    path('home/', include('home.urls')),
    path('api/', include('rest_framework.urls')),


] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
