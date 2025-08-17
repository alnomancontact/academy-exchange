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
from django.urls import path, include
from accounts.views import login_view, register_view , profile_view , history_view,  home_view, exchange_view, buy_item, about_view, contact_view
from django.contrib.auth.views import LogoutView # <-- Corrected: import register_view as well

urlpatterns = [
    path('exchange/', exchange_view, name='exchange'),
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),   
    path('accounts/login/', login_view, name='account_login'),        # Root URL now points to home page
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('profile/', profile_view, name='profile'),
    path('history/', history_view, name='history'),
     path('logout/', LogoutView.as_view(next_page='/login/'), name='logout'),
     path('buy/<int:item_id>/', buy_item, name='buy_item'),
    
    path('about/', about_view, name='about'),
    
    path('contact/', contact_view, name='contact'),

]

