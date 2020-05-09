from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:blog_id>/', views.detail, name='detail'),
    path('Contact/',views.Contact,name='Contact'),
]