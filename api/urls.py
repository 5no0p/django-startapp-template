from django.urls import include, path

urlpatterns = [
    path('v1/', include('{{ app_name}}.api.v1.urls')),
]