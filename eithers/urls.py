from django.urls import path
from . import views

app_name = 'eithers'

urlpatterns = [
    # Read
    path('', views.index, name='index'),  # All List
    path('create/', views.create, name='create'),  # Save
    path('<int:question_pk>/vote/', views.vote, name="vote"),

]