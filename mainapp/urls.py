from django.urls import path
from mainapp.views import *
from category.views import *
import random
from django.views.decorators.cache import cache_page
app_name = 'dantorial'
urlpatterns = [

    path('', IndexView.as_view(), name='index'),
# user account
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', UserRegistrationView.as_view(), name='register'),

# profile view

    path('profile-edit/<int:pk>', cache_page(60 * 15)(PersonalProfileEditView.as_view()), name='profile-edit'),
    path('profile-info-edit/<int:pk>', cache_page(60 * 15)(ProfileInfoEditView.as_view()), name='profile-info-edit'),
    path('photo/', updateimage, name='photochange'),
    # path('photoview/', UpdateImageView.as_view(), name='photoview'),

# my profile view 

    path('userprofile/<int:pk>', cache_page(60 * 15)(UserProfileView.as_view()), name='userprofile'),
    path('profile/', cache_page(60 * 15)(ProfileView.as_view()), name='profile'),
    path('profile-info/', ProfileInfoView.as_view(), name='profile-info'),
    path('my-subject/', ProfileSubjectView.as_view(), name='my-subject'),
    path('my-experience/', ProfileExperienceView.as_view(), name='my-experience'),
    path('my-qualification/', ProfileQualificationView.as_view(), name='my-qualification'),
    path('my-verification/', ProfileVerificationView.as_view(), name='my-verification'),
    path('my-availability/', ProfileAvailabilityView.as_view(), name='my-availability'),

    path('myaccount/', MyAccount.as_view(), name='my-account'),
    path('favourites/', FavouriteView.as_view(), name='myfavourites'),
# add view

    path('add-qualification/', QualificationAddView.as_view(), name='add-qualification'),
    path('add-experience/', ExperienceAddView.as_view(), name='add-experience'),
    path('add-subject/', SubjectAddView.as_view(), name='add-subject'),
    path('add-verification/', VerificationAddView.as_view(), name='add-verification'),
    path('add-availability/', AvailabilityAddView.as_view(), name='add-availability'),

# update view

    path(f'update/subject-{random.randint(10000,99999)}<int:pk>{random.randint(10000,99999)}/', SubjectUpdateView.as_view(), name='update_subject'),
    path(f'update/qualification-{random.randint(10000,99999)}<int:pk>{random.randint(10000,99999)}/', QualificationUpdateView.as_view(), name='update_qualification'),
    path(f'update/experience-{random.randint(10000,99999)}<int:pk>{random.randint(10000,99999)}/', ExperienceUpdateView.as_view(), name='update_experience'),
    path(f'update/verification-{random.randint(10000,99999)}<int:pk>{random.randint(10000,99999)}/', VerificationUpdateView.as_view(), name='update_verification'),
    path(f'update/availability-{random.randint(10000,99999)}<int:pk>{random.randint(10000,99999)}/', AvailabilityUpdateView.as_view(), name='update_availability'),

# delete views

    path('delete/subject-<int:pk>', SubjectDeleteView.as_view(), name='delete_subject'),
    path('delete/profile-<int:pk>', ProfileDeleteView.as_view(), name='delete_profile'),
    path('delete/experience-<int:pk>', ExperienceDeleteView.as_view(), name='delete_experience'),
    path('delete/qualification-<int:pk>', QualificationDeleteView.as_view(), name='delete_qualification'),
    path('delete/verification-<int:pk>', VerificationDeleteView.as_view(), name='delete_verification'),
    path('delete/availability-<int:pk>', AvailabilityDeleteView.as_view(), name='delete_availability'),

# serach view
    path('search/', cache_page(60 * 15)(SearchView.as_view()), name='search'),
    path('filter/', cache_page(60 * 15)(FilterView.as_view()), name='filter'),
    path('search/all/', cache_page(60 * 15)(SearchAllView.as_view()), name='allsearch'),

# category urls

    path('category/<slug:slug>/', cache_page(60 * 15)(CategoryView.as_view()), name='category'),
    path('sub/<category_slug>/<subcat_slug>/', cache_page(60 * 15)(SubcategoryView.as_view()), name='subcategory'),
    path('subj/<category_slug>/<subcat_slug>/<subject_slug>/', cache_page(60 * 15)(SubjectView.as_view()), name='subject'),
    path('allcategory', cache_page(60 * 15)(AllCategoryView.as_view()), name='allcategory'),
    path('allsubcategory', cache_page(60 * 15)(AllSubCategoryView.as_view()), name='allsubcategory'),
    path('allsubject', cache_page(60 * 15)(AllSubjectView.as_view()), name='allsubject'),

# contact us

    path('contact-us', cache_page(60 * 15)(ContactView.as_view()), name='contactus'),  
    path('about-us', cache_page(60 * 15)(AboutView.as_view()), name='aboutus'),
    path('privacy', cache_page(60 * 15)(PrivacyView.as_view()), name='privacy_policy'),
    path('terms-and-conditions', cache_page(60 * 15)(TermsView.as_view()), name='terms'),

# payment and support
    path('upgrade/', cache_page(60 * 15)(UpgradeAccountView.as_view()), name='upgrade_profile'),
    path('payment-success/', cache_page(60 * 15)(PaymentSuccessView.as_view()), name='pay-success'),
    path('payment-fail/', cache_page(60 * 15)(PaymentFailView.as_view()), name='pay-fail'),

# profile viewed
    path('profview/', cache_page(60 * 15)(ProfileViewList.as_view()), name='profview'),
    path('like/', cache_page(60 * 15)(profile_like), name='favourite'),
]