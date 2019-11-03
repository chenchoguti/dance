"""baile URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from .routers import router
from django.conf.urls.static import static
from django.conf import settings
from users import views as users_view
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('bailarina', TemplateView.as_view(template_name='indexBailarina.html')),
    path('teatro', TemplateView.as_view(template_name='indexTeatro.html')),
    path('users/login',users_view.login_view, name='login')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
