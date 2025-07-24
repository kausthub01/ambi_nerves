from django.urls import path
from . import views

app_name = 'mylumora'   # optional, but useful for namespacing

urlpatterns = [
    path('', views.index, name='index'),           # /myapp/
]