__author__ = 'Pavan Kotehal'

from django.urls import path
from . import views
urlpatterns = [
    path('api/lead/', views.LeadListCreate.as_view() ),
]