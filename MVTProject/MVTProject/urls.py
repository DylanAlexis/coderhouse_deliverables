from django.contrib import admin
from django.urls import path
from MVTProject.views import templateTest

urlpatterns = [
    path('admin/', admin.site.urls),
    path('templateTest', templateTest)
]
