from django.urls import path
from . import views
urlpatterns = [
    path('events/', views.HomeView.as_view(), name='home'),
    path('events/<int:pk>/', views.HomeView.as_view(), name='home-detail')

]
