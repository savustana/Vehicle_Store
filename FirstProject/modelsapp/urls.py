"""
URL configuration for FirstProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.HomePage.as_view(), name='index'),
    path('motorcycles', views.HomePageBike.as_view(), name='motorcycles'),
    path('about/', views.about, name='about'),
    path('register/', views.register, name='register'),
    path('login/', views.login_page, name='login'),
    path('stats/', views.stats, name='stats'),
    path('logout/', views.logout_page, name='logout'),
    path('add_car/', views.CarCreateView.as_view(), name='add_car'),
    path('info_car/<int:car_id>', views.info_car, name='info_car'),
    path('add_bike/', views.BikeCreateView.as_view(), name='add_bike'),
    path('bike_info/<int:bike_id>', views.bike_info, name='bike_info'),
    path('delete_car/<int:pk>', views.delete_car, name='delete_car'),
    path('delete_bike/<int:pk>', views.delete_bike, name='delete_bike'),

]

urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
