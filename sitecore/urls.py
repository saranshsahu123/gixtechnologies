from django.contrib import admin
from django.urls import path
from account import views

urlpatterns = [
    path('', views.applicant_form, name='applicant_form'),
    path('admin/', admin.site.urls),
]
