from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views


urlpatterns = [
	 path('adtobs/', views.AD_BS.as_view()),
	 path('bstoad/', views.BS_AD.as_view()),
	 path('childgrant/', views.ChildGrant.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)