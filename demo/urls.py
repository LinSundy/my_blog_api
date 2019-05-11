from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.hello),
    path('demo/', views.LoginView.as_view())
]
