
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('Stores.urls',namespace='Stores')),     
    path('location/',include('Location.urls')),
    path('user/', include('UserApp.urls',namespace='account')),
    path('product/',include('Products.urls')),
    #path('order/', include('OrderApp.urls')),
    path('order/', include('OrderApp.urls',namespace='OrderApp')),
    
    
    
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)