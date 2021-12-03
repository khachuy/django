from django.urls import path

from . import views

urlpatterns = [
    path('', views.get_all),
    path('insert', views.insert_member_dummy)
]