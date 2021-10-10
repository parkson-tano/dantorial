from mainapp.models import ProfilePersonal, ProfileInfo, Subject, Qualification, Experience
from django.contrib.auth.models import User
from rest_framework import serializers
from category.models import Category

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