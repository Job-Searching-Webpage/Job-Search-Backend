from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
   
   # API GET
    path('spotlights/', views.spotlightsGetAll, name='spotlightsGetAll'),
    path('teams/', views.teamsGetAll, name='teamsGetAll'),
    
    path('degrees/', views.degreesGetAll, name='degreesGetAll'),
    path('jobs/', views.jobsGetAll, name='jobsGetAll'),
    path('backUpPerson/', views.backUpPersonGetAll, name='backUpPersonGetAll'),
    path('esperienze/', views.esperienzeGetAll, name='esperienzeGetAll'),

    # API Get one 
    path('getJob_by_Id/<int:pk>/', views.getJob_by_Id, name='getJob_by_Id'),
    path('getTeam_by_Id/<int:pk>/', views.getTeam_by_Id, name='getTeam_by_Id'),


    #API POST
    path('saveTeam/', views.teamsSave, name='teamsSave'),
    path('saveBackUpPerson/', views.backUpPersonSave, name='backUpPersonSave'),
    path('JobSave/', views.JobSave, name='JobSave'),
    path('EsperienzeSave/', views.EsperienzeSave, name='EsperienzeSave'),

]