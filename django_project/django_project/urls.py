from django.contrib import admin
from django.urls import path, include
from bucket_list import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('bucket_list.urls')),
]
