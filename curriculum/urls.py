from django.urls import path
from . import views

urlpatterns = [
    path('', views.curriculum, name='curriculum'),
    path('<int:course_id>/', views.course, name='course'),
    path('add-link/<int:course_id>/', views.add_course_link, name='add_course_link'),
    path('delete/<int:course_id>/', views.delete_course, name='delete_course'),
    path('edit/<int:course_id>/', views.edit_course, name='edit_course'),
]