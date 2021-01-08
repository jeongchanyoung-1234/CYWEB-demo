
from django.urls import path, include
from django.contrib import admin
from pybo.views import base_views
from pybo import views

urlpatterns = [
    path('', base_views.index, name='index'),
    path('admin/', admin.site.urls),
    path('pybo/', include('pybo.urls')),
    path('common/', include('common.urls'))
]
