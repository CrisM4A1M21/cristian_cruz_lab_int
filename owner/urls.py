from django.urls import path
from owner import views

urlpatterns = [
    path('owner_list/', views.owner_list, name='owner_list')
]

