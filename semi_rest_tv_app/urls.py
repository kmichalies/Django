from django.urls import path,include
from  . import views

urlpatterns = [
    path('',views.shows),
    path('shows/new',views.new),
    path('shows/create',views.create),
    path('shows/<int:id>',views.oneshow),
    path('shows/',views.shows),
    path('shows/<int:id>/edit',views.edit),
    path('shows/<int:id>/update',views.update),
    path('shows/<int:id>/remove',views.destroy),
]