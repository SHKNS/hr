"""project URL Configuration

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
from django.urls import path, include, re_path
from rest_framework import routers
from test_app import views


router = routers.DefaultRouter()
router.register(r'tests', views.TestViewSet)
router.register(r'oversee', views.OverseeViewSet)

#######################################################

router.register(r'fm', views.FmViewSet)
router.register(r'pp', views.PpViewSet)
router.register(r'cool', views.CoolViewSet)
router.register(r'ruli', views.RuliViewSet)

#######################################################

router.register(r'auction', views.AuctionViewSet)
router.register(r'coupang', views.CoupangViewSet)
router.register(r'eleven', views.ElevenViewSet)
router.register(r'gmarket', views.GmarketViewSet)


urlpatterns = [
    path('test_app/', include('test_app.urls')),
    path('',include(router.urls)),
    path('admin/', admin.site.urls),
]
