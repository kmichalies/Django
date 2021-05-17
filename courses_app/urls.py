from django.urls import path
from  . import views

urlpatterns = [
    path('',views.courses),
    path('courses/create',views.create),
    path('courses/destroy/<int:id>',views.destroy),
    path('courses/destroy/delete_yes/<int:id>',views.delete_yes),
]