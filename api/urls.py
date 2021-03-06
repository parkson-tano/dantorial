from django.urls import path
from .views import *
urlpatterns = [
    path('', UserView.as_view({'get': 'list','post':'create'}), name='user'),
    path('<int:pk>', UserView.as_view({'get':'retrieve', 'patch':'partial_update', 'delete':'destroy', 'put':'update'})),
    path('prof/', ProfilePersonalView.as_view({'get': 'list', 'post':'create'}), name='profile'),
    path('prof/<int:pk>', ProfilePersonalView.as_view({'get':'retrieve', 'patch':'partial_update', 'delete':'destroy', 'put':'update'})),
    path('info/', ProfileInfoView.as_view({'get': 'list', 'post':'create'}), name='info'),
    path('info/<int:pk>', ProfileInfoView.as_view({'get':'retrieve', 'patch':'partial_update', 'delete':'destroy', 'put':'update'})),
    path('subject', SubjectView.as_view({'get': 'list', 'post':'create'}), name='subject'),
    path('subject/<int:pk>', SubjectView.as_view({'get':'retrieve', 'patch':'partial_update', 'delete':'destroy', 'put':'update'})),
    path('qualification', QualificationView.as_view({'get': 'list', 'post':'create'}), name='qualification'),
    path('qualification/<int:pk>', QualificationView.as_view({'get':'retrieve', 'patch':'partial_update', 'delete':'destroy', 'put':'update'})),
    path('experience', ExperienceView.as_view({'get': 'list', 'post':'create'}), name='experience'),
    path('experience/<int:pk>', ExperienceView.as_view({'get':'retrieve', 'patch':'partial_update', 'delete':'destroy', 'put':'update'})),
    path('cat/', CategoryView.as_view({'get': 'list', 'post':'create'}), name='category'),
    path('cat/<int:pk>/', CategoryView.as_view({'get':'retrieve', 'patch':'partial_update', 'delete':'destroy', 'put':'update'})),
    path('subcat/', SubCategoryView.as_view({'get': 'list', 'post':'create'}), name='subcategory'),
    path('subcat/<int:pk>/', SubCategoryView.as_view({'get':'retrieve', 'patch':'partial_update', 'delete':'destroy', 'put':'update'})),
    path('subj', AllSubjectView.as_view({'get': 'list', 'post':'create'}), name='allsubject'),
    path('country', CountryView.as_view({'get': 'list', 'post':'create'}), name='country'),
    path('country/<int:pk>', CountryView.as_view({'get':'retrieve', 'patch':'partial_update', 'delete':'destroy', 'put':'update'})),
    path('region', RegionView.as_view({'get': 'list', 'post':'create'}), name='region'),
    path('region/<int:pk>', RegionView.as_view({'get':'retrieve', 'patch':'partial_update', 'delete':'destroy', 'put':'update'})),
    path('town/', TownView.as_view({'get': 'list', 'post':'create'}), name='town'),
    path('town/<int:pk>/', TownView.as_view({'get':'retrieve', 'patch':'partial_update', 'delete':'destroy', 'put':'update'})),
    path('quater/', QuaterView.as_view({'get': 'list', 'post':'create'}), name='quater'),
    path('quater/<int:pk>/', QuaterView.as_view({'get':'retrieve', 'patch':'partial_update', 'delete':'destroy', 'put':'update'})),
    ]