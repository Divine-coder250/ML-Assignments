from django.urls import path
from . import views

urlpatterns = [
    path('', views.tenant_list, name='tenant_list'),
    path('create/', views.tenant_create, name='tenant_create'),
    path('<int:id>/update/', views.tenant_update, name='tenant_update'),
    path('<int:id>/delete/', views.tenant_delete, name='tenant_delete'),
]
