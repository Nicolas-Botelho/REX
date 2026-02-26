"""
URL configuration for rex project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from django.urls import include
from rest_framework import permissions, routers
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from rex.views.requirements_view import FunctionalRequirementViewSet, NonFunctionalRequirementViewSet, BusinessRulesViewSet
from rex.views.testcase_view import TestCaseViewSet
from rex.views.userstory_view import EpicViewSet, UserStoryViewSet, ActorViewSet

schema_view = get_schema_view(
   openapi.Info(
      title="REX API",
      default_version='v1',
      description="OpenAPI for REX",
      contact=openapi.Contact(email="contact@snippets.local"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

requirement_router = routers.DefaultRouter()

# Requirements
requirement_router.register('functional_requirement', FunctionalRequirementViewSet, basename='functional_requirement')
requirement_router.register('non_functional_requirement', NonFunctionalRequirementViewSet, basename='non_functional_requirement')
requirement_router.register('business_rules', BusinessRulesViewSet, basename='business_rules')
# Test Case
requirement_router.register('test_case', TestCaseViewSet, basename='test_case')
# User Story
requirement_router.register('epic', EpicViewSet, basename='epic')
requirement_router.register('user_story', UserStoryViewSet, basename='user_story')
requirement_router.register('actor', ActorViewSet, basename='actor')

urlpatterns = [
   path("", schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path("requirements/", include(requirement_router.urls))
]