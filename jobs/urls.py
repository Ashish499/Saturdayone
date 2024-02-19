from django.contrib import admin
from django.urls import path
from . import views

app_name="jobs"
urlpatterns=[
    path('',views.JobList.as_view(),name="index"),
    path('<int:pk>',views.JobDetailView.as_view(),name="detail"),
    path('create/',views.JobDetailView.as_view(),name="job_create"),
    path('<int:pk>/update/',views.JobDetailView.as_view(),name="job_update"),
    path('<int:pk>/delete/',views.JobDetailView.as_view(),name="job_delete")
    
]

