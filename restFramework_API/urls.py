"""restframework_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include
from django.views.generic.base import TemplateView
from rest_api import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('admin/', admin.site.urls),
    path('rest_example/', include('rest_framework.urls')),
    # path('welcome/', TemplateView.as_view(template_name='welcome.html')),
    # path('employeeoperation/', csrf_exempt(views.EmployeeOperation.as_view())),
    path('readallemployee/', views.ReadAllEmployee.as_view() , name="readallemployee"),
    path('readoneemployee/<int:employee>/', views.ReadOneEmployee.as_view(), name="readoneemployee"),
    path('updateemployee/<int:employee>/', csrf_exempt(views.UpdateEmployee.as_view())),
    path('deleteemployee/<int:employee>/', csrf_exempt(views.DeleteEmployee.as_view())),
    
]
