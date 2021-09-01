from django.urls import path
from mainapp.views import *
from category.views import *
app_name = 'dantorial'
urlpatterns = [

    path('', IndexView.as_view(), name='index'),
# user account
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', UserRegistrationView.as_view(), name='register'),

# profile view

    path('profile-edit/<int:pk>', PersonalProfileEditView.as_view(), name='profile-edit'),
    path('profile-info-edit/<int:pk>', ProfileInfoEditView.as_view(), name='profile-info-edit'),

# my profile view 

    path('userprofile/<int:pk>', UserProfileView.as_view(), name='userprofile'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('profile-info/', ProfileInfoView.as_view(), name='profile-info'),
    path('my-subject', ProfileSubjectView.as_view(), name='my-subject'),
    path('my-experience', ProfileExperienceView.as_view(), name='my-experience'),
    path('my-qualification', ProfileQualificationView.as_view(), name='my-qualification'),

    path('myaccount/', MyAccount.as_view(), name='my-account'),

# add view

    path('add-qualification', QualificationEditView.as_view(), name='add-qualification'),
    path('add-experience', ExperienceEditView.as_view(), name='add-experience'),
    path('add-subject', SubjectEditView.as_view(), name='add-subject'),


# update view

    path('update/subject-<int:pk>', SubjectUpdateView.as_view(), name='update_subject'),
    path('update/qualification-<int:pk>', QualificationUpdateView.as_view(), name='update_qualification'),
    path('update/experience-<int:pk>', ExperienceUpdateView.as_view(), name='update_experience'),

# delete views

    path('delete/subject-<int:pk>', SubjectDeleteView.as_view(), name='delete_subject'),
    path('delete/profile-<int:pk>', ProfileDeleteView.as_view(), name='delete_profile'),
    path('delete/experience-<int:pk>', ExperienceDeleteView.as_view(), name='delete_experience'),
    path('delete/qualification-<int:pk>', QualificationDeleteView.as_view(), name='delete_qualification'),

# serach view
    path('search/', SearchView.as_view(), name='search'),

# category urls

    path('category/<slug:slug>', CategoryView.as_view(), name='category'),
    path('subcategory/<slug:slug>', SubcategoryView.as_view(), name='subcategory'),
    path('subject/<slug:slug>', SubjectView.as_view(), name='subject'),
]