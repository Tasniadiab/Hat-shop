from django.urls import path
from .views import api_list_shoes, api_shoe_detail

urlpatterns = [
    path("shoes/", api_list_shoes, name="api_list_shoes"),
    path("bins/<int:bin_vo_id>/shoes/", api_list_shoes, name="api_list_shoe"),
    path("shoes/<int:pk>/", api_shoe_detail, name="api_shoe_detail"),
]
