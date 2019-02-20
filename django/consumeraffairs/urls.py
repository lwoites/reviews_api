"""consumeraffairs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from rest_framework.authtoken import views
from consumeraffairs.reviews.views import CompanyDetail, CompanyList, ReviewDetail, ReviewList

api_v1_urls = [
    path('reviews/', ReviewList.as_view(), name="review-list"),
    path('reviews/<int:pk>/', ReviewDetail.as_view(), name="review-details"),
    path('companies/', CompanyList.as_view(), name="company-list"),
    path('companies/<int:pk>/', CompanyDetail.as_view(), name="company-detail")
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api-token-auth/', views.obtain_auth_token),
    path('api/v1/', include(api_v1_urls)),
]
