from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:log_id>/', views.log, name='log'),
    path('glosary/', views.glosary, name='glosary'),
    path('term/<int:term_id>/', views.term, name='term'),
    path('tips/', views.tips, name='tips')
]