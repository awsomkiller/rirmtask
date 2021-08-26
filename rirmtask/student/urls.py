from . import views
from django.urls import path


urlpatterns = [
    path('', views.home, name="home"),
    path('addstudent/', views.addStudent),
    path('addacademic/', views.addAcademic),
    path('viewdata/', views.viewData),
    # path('login/',views.login),
    # path('logout/',views.logout),
    path('register/',views.register),
]
