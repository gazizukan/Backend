from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework.parsers import JSONParser

from api.models import Member, User, City, Company, Station, Review
from api.serializers import MemberSerializer, UserSerializer, CitySerializer
from api.serializers import CompanySerializer, StationSerializer, ReviewSerializer

@csrf_exempt
def member_list(request):
  if request.method == "GET":
    members = Member.objects.all()
    ser = MemberSerializer(members, many=True)
    return JsonResponse(ser.data, safe=False)
  elif request.method == "POST":
    data = JSONParser().parse(request)
    ser = MemberSerializer(data=data)
    if ser.is_valid():
      ser.save()
      return JsonResponse(ser.data, status=201)
    return JsonResponse(ser.errors, status=400)

@csrf_exempt
def user_list(request):
  if request.method == "GET":
    users = User.objects.all()
    ser = UserSerializer(users, many=True)
    return JsonResponse(ser.data, safe=False)
  elif request.method == "POST":
    data = JSONParser().parse(request)
    ser = UserSerializer(data=data)
    if ser.is_valid():
      ser.save()
      return JsonResponse(ser.data, status=201)
    return JsonResponse(ser.errors, status=400)

@csrf_exempt
def city_list(request):
  if request.method == "GET":
    cities = City.objects.all()
    ser = CitySerializer(cities, many=True)
    return JsonResponse(ser.data, safe=False)
  elif request.method == "POST":
    data = JSONParser().parse(request)
    ser = CitySerializer(data=data)
    if ser.is_valid():
      ser.save()
      return JsonResponse(ser.data, status=201)
    return JsonResponse(ser.errors, status=400)

@csrf_exempt
def company_list(request):
  if request.method == "GET":
    companies = Company.objects.all()
    ser = CompanySerializer(companies, many=True)
    return JsonResponse(ser.data, safe=False)
  elif request.method == "POST":
    data = JSONParser().parse(request)
    ser = CompanySerializer(data=data)
    if ser.is_valid():
      ser.save()
      return JsonResponse(ser.data, status=201)
    return JsonResponse(ser.errors, status=400)

@csrf_exempt
def station_list(request):
  if request.method == "GET":
    stations = Station.objects.all()
    ser = StationSerializer(stations, many=True)
    return JsonResponse(ser.data, safe=False)
  elif request.method == "POST":
    data = JSONParser().parse(request)
    ser = StationSerializer(data=data)
    if ser.is_valid():
      ser.save()
      return JsonResponse(ser.data, status=201)
    return JsonResponse(ser.errors, status=400)

@csrf_exempt
def review_list(request):
  if request.method == "GET":
    reviews = Review.objects.all()
    ser = ReviewSerializer(reviews, many=True)
    return JsonResponse(ser.data, safe=False)
  elif request.method == "POST":
    data = JSONParser().parse(request)
    ser = ReviewSerializer(data=data)
    if ser.is_valid():
      ser.save()
      return JsonResponse(ser.data, status=201)
    return JsonResponse(ser.errors, status=400)