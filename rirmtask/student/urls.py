from . import views
from django.urls import path


urlpatterns = [
    path('', views.home, name="home"),
    path('addstudent/', views.addStudent),
    path('addacademic/', views.addAcademic),
    path('viewdata/', views.viewData),
]
