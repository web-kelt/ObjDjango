from django.urls import path, include, re_path

from . import views


urlpatterns = [
    path('', views.index),
    
    #path('<int:article_id>/', views.detail, name='detail'),
    #path('<int:article_id>/leave_comment/', views.leave_comment, name='leave_comment'),
    #path('<int:article_id>/upload/', views.upload, name='upload')
]
