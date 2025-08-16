"""
URL configuration for exchange project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
# In your urls.py (e.g., exchange/urls.py)

from django.contrib import admin
from django.urls import path
from accounts.views import login_view, register_view , profile_view , history_view # <-- Corrected: import register_view as well

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login_view, name='home'), # Changed name to 'home' if this is your root/landing page
    path('login/', login_view, name='login'), # Added a dedicated /login/ path
    path('register/', register_view, name='register'),
  path('profile/', profile_view, name='profile'),
  path('history/', history_view, name='history'),

]

