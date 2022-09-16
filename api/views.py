from django.shortcuts import render
from .serializers import *
from mainapp.models import ProfilePersonal, ProfileInfo, Subject, Qualification, Experience
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
# from rest_framework.permissions import IsAd
from category.models import Category, SubCategory, Subject
from location.models import Country, Region, Town, Quater
# Create your views here.
from django.contrib.auth import get_user_model
User = get_user_model()

class UserView(viewsets.ModelViewSet):
    authentication_classes = (
        SessionAuthentication, BasicAuthentication, TokenAuthentication)
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # permission_classes = (IsAdminOrReadOnly,)


class ProfilePersonalView(viewsets.ModelViewSet):
    queryset = ProfilePersonal.objects.all()
    serializer_class = ProfilePersonalSerializer


class ProfileInfoView(viewsets.ModelViewSet):
    queryset = ProfileInfo.objects.all()
    serializer_class = ProfileInfoSerializer


class SubjectView(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


class QualificationView(viewsets.ModelViewSet):
    queryset = Qualification.objects.all()
    serializer_class = QualificationSerializer


class ExperienceView(viewsets.ModelViewSet):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer


class CategoryView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class SubCategoryView(viewsets.ModelViewSet):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer


class AllSubjectView(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = AllSubjectSerializer


class CountryView(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class RegionView(viewsets.ModelViewSet):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer


class TownView(viewsets.ModelViewSet):
    queryset = Town.objects.all()
    serializer_class = TownSerializer


class QuaterView(viewsets.ModelViewSet):
    queryset = Quater.objects.all()
    serializer_class = QuaterSerializer
