from django.urls import path
from mainapp.views import *
from category.views import *
import random
from django.views.decorators.cache import cache_page
from django.contrib.sitemaps.views import sitemap
from .sitemap import *
app_name = 'dantorial'

sitemaps = {
    'category': CategorySitemap,
    # 'subcategory': SubCategorySitemap,
    'subject': SubjectSitemap,
    'static':StaticSitemap
}

urlpatterns = [

    path('', IndexView.as_view(), name='index'),
# user account
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', UserRegistrationView.as_view(), name='register'),

# profile view

    path('profile-edit/<int:pk>', PersonalProfileEditView.as_view(), name='profile-edit'),
    path('profile-info-edit/<int:pk>', ProfileInfoEditView.as_view(), name='profile-info-edit'),
    path('photo/', updateimage, name='photochange'),
    # path('photoview/', UpdateImageView.as_view(), name='photoview'),

# my profile view 

    path('userprofile/<int:pk>/', UserProfileView.as_view(), name='userprofile'),
    path('profile/', ProfileView.as_view(), name='profile'),
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
    path('search/', SearchView.as_view(), name='search'),
    path('filter/', FilterView.as_view(), name='filter'),
    path('search/all/', SearchAllView.as_view(), name='allsearch'),

# category urls

    path('category/<slug:slug>/', CategoryView.as_view(), name='category'),
    path('sub/<category_slug>/<subcat_slug>/', SubcategoryView.as_view(), name='subcategory'),
    path('subj/<category_slug>/<subcat_slug>/<subject_slug>/', SubjectView.as_view(), name='subject'),
    path('allcategory', AllCategoryView.as_view(), name='allcategory'),
    path('allsubcategory', AllSubCategoryView.as_view(), name='allsubcategory'),
    path('allsubject', AllSubjectView.as_view(), name='allsubject'),
    path('region/<int:pk>', FilterRegionView.as_view(), name='region'),

# contact us

    path('contact-us', ContactView.as_view(), name='contactus'),  
    path('about-us', AboutView.as_view(), name='aboutus'),
    path('privacy', PrivacyView.as_view(), name='privacy_policy'),
    path('terms-and-conditions', TermsView.as_view(), name='terms'),
    path('landing', LandingView.as_view(), name='landing'),

# payment and support
    path('upgrade/', UpgradeAccountView.as_view(), name='upgrade_profile'),
    path('payment-success/', PaymentSuccessView.as_view(), name='pay-success'),
    path('payment-fail/', PaymentFailView.as_view(), name='pay-fail'),

# profile viewed
    path('profview/', ProfileViewList.as_view(), name='profview'),
    path('like/', profile_like, name='favourite'),


# schedule 
    path('schedule/<int:pk>', ScheduleView.as_view(), name='schedule'),
    path('request/', OnlineLessonNotification.as_view(), name='notification'),
    path('request/<int:pk>', NotificationDetail.as_view(), name='notification_detail'),
    path('request_history/', OnlineLessonRequest.as_view(), name='request_history'),

    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('price/', PriceView.as_view(), name='price'),
    path('loaderio-c1a185840f545fea9a1f72d3524a5531/', load_test),
]

