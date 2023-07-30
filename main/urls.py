from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from trade.views import JSONResponse
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('common.urls')),
    path('api/v1/chios/',JSONResponse.commdity_list)
]
