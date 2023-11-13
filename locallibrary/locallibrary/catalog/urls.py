
from django.conf import settings
from django.conf.urls.static import static

from django.urls import path
from . import views
from .views import validate_username
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from django.urls import re_path as url
from .views import *

urlpatterns = [
    path('', ApplicationListView.as_view(), name='index'),
    path('login/', LoginView.as_view(), name='login'),
    path('registration/', views.registration, name='registration'),
    path('register', views.RegisterView.as_view(), name='register'),
    path('validate_username', validate_username, name='validate_username'),
    path('logout/', BBLogoutView.as_view(), name='logout'),
    path('profil/', ApplicationsByUserListView.as_view(), name='profil'),

    path('request/', views.ApplicationCreate.as_view(), name='request'),
    path('creating/', views.MyPostListViews.as_view(), name='creating'),
    path('deleting/', views.ApplicationDelete.as_view(), name='deleting'),

    path('admin_base/', views.ApplicationListViewAdmin.as_view(), name='admin_base'),
    path('category/', views.CategoryView.as_view(), name='category'),
    path('category/<int:pk>/delete/', views.CategoryDelete.as_view(), name='category_delete'),
    path('creating_category/', views.CategoryCreate.as_view(), name='creating_category'),
    path('change/<int:pk>/status/', views.ChangeStatusRequest.as_view(), name='change_status'),
    path('request/<int:pk>/delete/', views.ApplicationDelete.as_view(), name='application_confirm_delete')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

