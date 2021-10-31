from django.shortcuts import render
from .serializers import *
from mainapp.models import ProfilePersonal, ProfileInfo, Subject, Qualification, Experience
from rest_framework import viewsets
from category.models import Category, SubCategory, Subject
# Create your views here.

class UserView(viewsets.ModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer

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