"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from mechanics.views import (
    get_mechanics,
    get_mechanic,
    update_mechanic,
    delete_mechanic,
    service_requests,
    get_service_request,
    update_service_request
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/mechanics/', get_mechanics),
    path('api/mechanics/<int:id>/update/', update_mechanic),
    path('api/mechanics/<int:id>/', get_mechanic),
    path('api/mechanics/<int:id>/delete/', delete_mechanic),
    path('api/service-requests/', service_requests),
    path('api/service-requests/<int:id>/', get_service_request),
    path('api/service-requests/<int:id>/update/', update_service_request),
]

