from . import views
from django.urls import path, include


urlpatterns = [
    path('', views.index, name='index'),
    path('<int:contact_id>', views.view_contact, name='view_contact'),
]