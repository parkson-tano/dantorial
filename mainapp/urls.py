from django.urls import path
from mainapp.views import *
from category.views import *
app_name = 'dantorial'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('profile-edit/<int:pk>', PersonalProfileEditView.as_view(), name='profile-edit'),
    path('profile-info-edit/<int:pk>', ProfileInfoEditView.as_view(), name='profile-info-edit'),
    path('add-subject', SubjectEditView.as_view(), name='add-subject'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('profile-info/', ProfileInfoView.as_view(), name='profile-info'),
    path('my-subject', ProfileSubjectView.as_view(), name='my-subject'),
    path('userprofile/<int:pk>', UserProfileView.as_view(), name='userprofile'),

    # category urls
    path('category/<slug:slug>', CategoryView.as_view(), name='category'),
    path('subcategory/<slug:slug>', SubcategoryView.as_view(), name='subcategory'),
    path('subject/<slug:slug>', SubjectView.as_view(), name='subject'),
]