from django.contrib import admin
from django.urls import path, include
from .import views

urlpatterns = [   

    # Маршруты для работы с людьми 
    path('', views.human_list, name='human_list'),
    path('add/', views.add_human, name='add_human'),
    path('human/<int:pk>/', views.human_detail, name='human_detail'),
    path('human/<int:pk>/delete/', views.delete_human, name='delete_human'),
    path('human/<int:pk>/edit/', views.edit_human, name='edit_human'),

    # Маршруты для работы с городами
    path('city_list/', views.city_list, name='city_list'),
    path('add_city/', views.add_city, name='add_city'),
    path('city/<int:pk>/', views.city_detail, name='city_detail'),
    path('city/<int:pk>/delete/', views.delete_city, name='delete_city'),
    path('city/<int:pk>/edit/', views.edit_city, name='edit_city'),

    # Маршруты для работы со странами
    path('country_list/', views.country_list, name='country_list'),
    path('add_country/', views.add_country, name='add_country'),
    path('country/<int:pk>/', views.country_detail, name='country_detail'),
    path('country/<int:pk>/delete/', views.delete_country, name='delete_country'),
    path('country/<int:pk>/edit/', views.edit_country, name='edit_country'),
]
