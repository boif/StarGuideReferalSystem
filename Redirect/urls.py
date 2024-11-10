from django.urls import path
from Redirect import views

urlpatterns = [
    path('', views.redirect_view, name='redirect_view'),
]
