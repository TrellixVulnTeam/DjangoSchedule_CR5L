from . import views
from django.urls import path, include


urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search, name='search'),
    path('<int:contact_id>', views.view_contact, name='view_contact'),
]