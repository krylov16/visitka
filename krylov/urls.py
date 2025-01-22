
from django.urls import path
from visitka import views

urlpatterns = [
    path('', views.index),
    path('contact', views.contact),
    path('service', views.service),
    path('sertificates', views.sertificates),
    path('post_question', views.post_question),
]
