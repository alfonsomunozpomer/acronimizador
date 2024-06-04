from django.urls import path

from . import views

urlpatterns = [
    # ex: /
    path('', views.index, name='index'),
    # ex: /ola/
    path('<str:word>/', views.definition, name='definition'),
    # ex: /ola/definir/
    path('<str:word>/definir/', views.define, name='define'),
]
