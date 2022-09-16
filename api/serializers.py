from mainapp.models import ProfilePersonal, ProfileInfo, Subject, Qualification, Experience
from rest_framework import serializers
from category.models import Category, SubCategory, Subject
from location.models import Country, Region, Town, Quater
from django.contrib.auth import get_user_model
User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('id','username', 'email', 'password',)

class ProfileInfoSerializer(serializers.ModelSerializer):
	class Meta:
		model = ProfileInfo
		fields = "__all__"

class ProfilePersonalSerializer(serializers.ModelSerializer):
	class Meta:
		model = ProfilePersonal
		fields = "__all__"

class SubjectSerializer(serializers.ModelSerializer):
	class Meta:
		model = Subject
		fields = "__all__"

class QualificationSerializer(serializers.ModelSerializer):
	class Meta:
		model = Qualification
		fields = "__all__"

class ExperienceSerializer(serializers.ModelSerializer):
	class Meta:
		model = Experience
		fields = "__all__"

class CategorySerializer(serializers.ModelSerializer):
	class Meta:
		model = Category
		fields = "__all__"

class SubCategorySerializer(serializers.ModelSerializer):
	class Meta:
		model = SubCategory
		fields = ('id','category', 'name', 'slug', 'image', 'date_created',)

class AllSubjectSerializer(serializers.ModelSerializer):
	class Meta:
		model = Subject
		fields = "__all__"

class CountrySerializer(serializers.ModelSerializer):
	class Meta:
		model = Country
		fields = "__all__"

class RegionSerializer(serializers.ModelSerializer):
	class Meta:
		model = Region
		fields = "__all__"

class TownSerializer(serializers.ModelSerializer):
	class Meta:
		model = Town
		fields = ('id', 'name', 'region')

class QuaterSerializer(serializers.ModelSerializer):
	class Meta:
		model = Quater
		fields = "__all__"
