from rest_framework import serializers
from api.models import Member, User, City, Company, Station, Review

class MemberSerializer(serializers.ModelSerializer):
  
  class Meta:
    model = Member
    fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
  
  class Meta:
    model = User
    fields = '__all__'

class CitySerializer(serializers.ModelSerializer):
  
  class Meta:
    model = City
    fields = '__all__'

class CompanySerializer(serializers.ModelSerializer):
  
  class Meta:
    model = Company
    fields = '__all__'

class StationSerializer(serializers.ModelSerializer):
  
  class Meta:
    model = Station
    fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
  
  class Meta:
    model = Review
    fields = '__all__'