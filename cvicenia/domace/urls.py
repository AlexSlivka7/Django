from django.urls import path
from . import views

urlpatterns = [
    path('', views.domace, name='domace'),
    path('vizitka/', views.du2_, name='vizitka'),
    path('teplota/', views.du3_teplota, name='du3_teplota'),
]
