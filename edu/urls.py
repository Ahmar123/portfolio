from django.urls import path
from . import views
urlpatterns = [
	path('skill/', views.skils,name="skills")
]