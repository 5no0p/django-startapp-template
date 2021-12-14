from django.urls import include, path
from rest_framework import routers
from {{ app_name}}.api.v1 import views

router = routers.DefaultRouter()
#router.register(r'{{ app_name}}', views.{{ camel_case_app_name }}ViewSet)

urlpatterns = [
    path('', include(router.urls)),
]