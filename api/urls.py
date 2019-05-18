from django.urls import path, include

from api import views

urlpatterns = [
   path('members/', views.member_list),
   path('users/', views.user_list),
   path('cities/', views.city_list),
   path('companies/', views.company_list),
   path('stations/', views.station_list),
   path('reviews/', views.review_list)
]