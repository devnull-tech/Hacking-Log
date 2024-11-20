from . import views
from django.urls import path

urlpatterns = [
    path('', views.home_redirect),
    path('<int:log_id>', views.log, name='log'),
    path('vulnhub/', views.index, name='vulnhub_index'),
    path('hackthebox/', views.index, name='hackthebox_index'),
]