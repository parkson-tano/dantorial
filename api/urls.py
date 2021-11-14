from django.urls import path
from .views import *
urlpatterns = [
    path('', UserView.as_view({'get': 'list','post':'create'}), name='user'),
    path('<int:pk>', UserView.as_view({'get':'retrieve', 'patch':'partial_update', 'delete':'destroy', 'put':'update'})),
    path('prof/', ProfilePersonalView.as_view({'get': 'list', 'post':'create'}), name='user'),
    path('prof/<int:pk>', ProfilePersonalView.as_view({'get':'retrieve', 'patch':'partial_update', 'delete':'destroy', 'put':'update'})),
    path('info/', ProfileInfoView.as_view({'get': 'list', 'post':'create'}), name='user'),
    path('info/<int:pk>', ProfileInfoView.as_view({'get':'retrieve', 'patch':'partial_update', 'delete':'destroy', 'put':'update'})),
    path('subject', SubjectView.as_view({'get': 'list', 'post':'create'}), name='user'),
    path('subject/<int:pk>', SubjectView.as_view({'get':'retrieve', 'patch':'partial_update', 'delete':'destroy', 'put':'update'})),
    path('qualification', QualificationView.as_view({'get': 'list', 'post':'create'}), name='user'),
    path('qualification/<int:pk>', QualificationView.as_view({'get':'retrieve', 'patch':'partial_update', 'delete':'destroy', 'put':'update'})),
    path('experience', ExperienceView.as_view({'get': 'list', 'post':'create'}), name='user'),
    path('experience/<int:pk>', ExperienceView.as_view({'get':'retrieve', 'patch':'partial_update', 'delete':'destroy', 'put':'update'})),
    path('cat/', CategoryView.as_view({'get': 'list', 'post':'create'}), name='user'),
    path('cat/<int:pk>/', CategoryView.as_view({'get':'retrieve', 'patch':'partial_update', 'delete':'destroy', 'put':'update'})),
    path('subcat/', SubCategoryView.as_view({'get': 'list', 'post':'create'}), name='user'),
    path('subcat/<int:pk>/', SubCategoryView.as_view({'get':'retrieve', 'patch':'partial_update', 'delete':'destroy', 'put':'update'})),
        path('subj', AllSubjectView.as_view({'get': 'list', 'post':'create'}), name='user'),
    ]