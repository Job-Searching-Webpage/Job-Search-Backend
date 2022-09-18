from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import generics

# our framework will automatically look for a template called apiOverview.html
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

# serializers import 
from .serializers import spotlightsSerializer, esperienzeSerializer, teamsSerializer, backUpPersonSerializer, jobsSerializer, degreesSerializer, dipendenti_userSerializer

# Create your views here.
from .models import spotlights, esperienze, teams, backUpPerson, jobs, degrees, dipendenti_user

@api_view(['GET'])
def spotlightsGetAll(request):

    spotlightss = spotlights.objects.all()
    serializer = spotlightsSerializer(spotlightss, many=True)

    return Response(serializer.data)



@api_view(['GET'])
def esperienzeGetAll(request):
    esperienzess = esperienze.objects.all()
    serializer = esperienzeSerializer(esperienzess, many=True)
    
    return Response(serializer.data)

@api_view(['GET'])
def teamsGetAll(request):
    teamss = teams.objects.all()
    
    def parse_string_array(s):
        return [word.strip() for word in s.replace("\"", "").split(",")]

    return Response([{
        'CF': team.CF,
        'id': team.id,
        'name': team.name,
        'cognome': team.cognome,
        'dataNascita': team.dataNascita,
        'birthplace': team.birthplace,
        'nazionalita': team.nazionalita,
        'address': team.address,
        'jobType': team.jobType,
        'period': team.period,
        'phone': team.phone,
        'email': team.email,
        "languages": parse_string_array(team.languages),
        'patenta': team.patenta,
        'car': team.car,
        'qualification': team.qualification,
        #'experienze': esperienzeSerializer(esperienze.get(CF_team = team.CF), many=True)
        } for team in teamss], 
        )
        

@api_view(['GET'])
def backUpPersonGetAll(request):
    backuppersons = backUpPerson.objects.all()
    serializer = backUpPersonSerializer(backuppersons, many=True)
            
    return Response(serializer.data)

  
@api_view(['GET'])
def jobsGetAll(request):

    jobss = jobs.objects.all()

    def parse_string_array(s):
        return [word.strip() for word in s.replace("\"", "").split(",\r\n")]

    return Response([{
        'id': job.id,
        'title': job.title,
        'organization': job.organization,
        'degree': job.degree,
        'jobType': job.jobType,
        'location': job.location,
                       
        "minimumQualifications": parse_string_array(job.minimumQualifications),
        "preferredQualifications": parse_string_array(job.preferredQualifications),
        "description": parse_string_array(job.description),
        "dateAdded": job.dateAdded,
        } for job in jobss], 
        )


@api_view(['GET'])
def degreesGetAll(request):
    degreess = degrees.objects.all()
    serializer = degreesSerializer(degreess, many=True)
                    
    return Response(serializer.data)


@api_view(['GET'])
def getJob_by_Id(request, pk):

    job = jobs.objects.get(id=pk)

    def parse_string_array(s):
        return [word.strip() for word in s.replace("\"", "").split(",\r\n")]

    return Response({
        'id': job.id,
        'title': job.title,
        'organization': job.organization,
        'degree': job.degree,
        'jobType': job.jobType,
        'location': job.location,
                       
        "minimumQualifications": parse_string_array(job.minimumQualifications),
        "preferredQualifications": parse_string_array(job.preferredQualifications),
        "description": parse_string_array(job.description),
        "dateAdded": job.dateAdded,
        })


@api_view(['GET'])
def getTeam_by_Id(request, pk):
    team = teams.objects.get(id=pk)
    serializer = teamsSerializer(team, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def teamsSave(request):
    serializer = teamsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def backUpPersonSave(request):
    serializer = backUpPersonSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def JobSave(request):
    serializer = jobsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def EsperienzeSave(request):
    serializer = esperienzeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)



