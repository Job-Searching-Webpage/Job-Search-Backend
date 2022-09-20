from rest_framework import serializers
from DBApp.models import spotlights, esperienze, teams, backUpPerson, jobs, degrees, dipendenti_user

class spotlightsSerializer(serializers.ModelSerializer):
       class Meta:
            model = spotlights
            fields = '__all__'

class esperienzeSerializer(serializers.ModelSerializer):
        class Meta:
             model = esperienze
             fields = '__all__'


class teamsSerializer(serializers.ModelSerializer):
            class Meta:
                model = teams
                fields = '__all__'
     
class backUpPersonSerializer(serializers.ModelSerializer):
               class Meta:
                    model = backUpPerson
                    fields = '__all__'

class jobsSerializer(serializers.ModelSerializer):
     class Meta:
          model = jobs
          fields = '__all__'

class degreesSerializer(serializers.ModelSerializer):
               class Meta:
                    model = degrees
                    fields = '__all__'
          
class dipendenti_userSerializer(serializers.ModelSerializer):
               class Meta:
                    model = dipendenti_user
                    fields = '__all__'



