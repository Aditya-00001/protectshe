from django.urls import path
from . import views

urlpatterns = [
    path('test-mongo/', views.test_connection_view, name='test-mongo'),
]
