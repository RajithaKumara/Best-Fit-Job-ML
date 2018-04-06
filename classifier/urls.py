from django.urls import path

# Init tensorflow model once for train
from .estimator import model
model.main([])

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contentClassification', views.classification, name='classification'),
]
