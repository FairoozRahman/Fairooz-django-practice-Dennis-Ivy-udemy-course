from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('', views.getRoutes),
    path('projects/', views.getProjects),
    path('projects/<str:pk>/', views.getProject),
    path('users/token/', TokenObtainPairView.as_view()),
    path('users/token/refresh/', TokenRefreshView.as_view()),
]
