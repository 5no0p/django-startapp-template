from django.urls import include, path
from rest_framework import routers
from {{ app_name}}.api.v1 import views

router = routers.DefaultRouter()
#router.register(r'tasks', views.TaskViewSet)

urlpatterns = [
    path('', include(router.urls)),
]