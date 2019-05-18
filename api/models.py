from django.conf import settings
from django.db import models
from django.utils import timezone

class Member(models.Model):
    member_first_name = models.CharField(max_length=50)
    member_second_name = models.CharField(max_length=50)
    position = models.CharField(max_length=100)
    member_img = models.CharField(max_length=200,default='https://i.ibb.co/G2LHm2P/1.png')

    def __str__(self):
        return self.member_first_name


class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.username


class City(models.Model):
    city_name = models.CharField(max_length=30)

    def __str__(self):
        return self.city_name


class Company(models.Model):
    company_id = models.CharField(max_length=130)
    company_name = models.CharField(max_length=100)
    company_img = models.CharField(max_length=400, default='https://ibb.co/G2LHm2P')
    company_rate_img = models.CharField(max_length=400, default='https://ibb.co/G2LHm2P')
    city = models.CharField(max_length=30)
    price_for_92 = models.FloatField()
    price_for_95 = models.FloatField()
    price_for_98 = models.FloatField()
    price_for_dt = models.FloatField()

    def __str__(self):
        return self.company_id



class Station(models.Model):
    company_id = models.CharField(max_length=130)
    address = models.CharField(max_length=200)
    station_logo = models.CharField(max_length=400, default='https://ibb.co/G2LHm2P') 
    station_img = models.CharField(max_length=400, default='https://ibb.co/G2LHm2P')
    station_tel = models.CharField(max_length=130,default='open 24 hours') 
    station_work_our = models.CharField(max_length=130,default='7242-17-65')  
    has_market = models.BooleanField()
    has_atm = models.BooleanField()
    has_wc = models.BooleanField()
    has_cafe = models.BooleanField()
    has_carwash = models.BooleanField()
    has_cto = models.BooleanField()
    has_term = models.BooleanField(default=True)
    has_beeline = models.BooleanField(default=True)
    has_qiwi = models.BooleanField(default=True)
    has_woopay = models.BooleanField(default=True)
    

    def __str__(self):
        return self.address


class Review(models.Model):
    station = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    content = models.TextField()
    mark = models.IntegerField()

    def publish(self):
        self.save()

    def __str__(self):
        return self.content


class Advert(models.Model):
    content = models.TextField(max_length=200)
    station = models.CharField(max_length=200)

    def __str__(self):
        return self.content
        

