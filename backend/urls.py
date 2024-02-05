from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('myinfo/<int:pk>', views.student_detail),
    path('myinfo/', views.all_student_detail),
    
]
