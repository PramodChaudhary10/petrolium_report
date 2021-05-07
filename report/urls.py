from django.urls import path
from report import views

urlpatterns = [
    path('', views.home, name='home'),
    path('jsondata/', views.fetch_json_data, name='jsondata'),
    path('databasedata/', views.database_data, name='databasedata'),
]
