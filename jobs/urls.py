from django.urls import path

from jobs import views

app_name = 'job_user'

urlpatterns = [
    path('', views.main_page, name='main_page'),

]