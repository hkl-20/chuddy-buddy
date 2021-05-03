import os, sys
from os.path import basename

from django.urls.conf import include
from django.views.generic import base
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from django.contrib import admin
from django.urls import path
from core import views
from rest_framework_simplejwt import views as jwt_views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'api/lists', views.ListsViewSet, basename='lists')
router.register(r'api/tasks', views.TasksViewSet, basename='tasks')
router.register(r'api/reminders', views.RemindersViewSet, basename='reminders')
router.register(r'api/flairs', views.FlairsViewSet, basename='flairs')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('hello/', views.HelloView.as_view(), name='hello'),
    path('api/create-user/', views.CreateUserView.as_view(), name='create-user'),
    path('', include(router.urls)),
]