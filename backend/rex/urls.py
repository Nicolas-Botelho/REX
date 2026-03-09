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

from rex.views.class_view import ClassViewSet, ClassAttributeEnumViewSet, ClassAttributePrimViewSet, EnumViewSet, EnumAttributeViewSet, RelationViewSet, RelationClassReferenceViewSet
from rex.views.usecase_view import ActorViewSet, EventViewSet, StepViewSet, UsecaseViewSet

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

class_router = routers.DefaultRouter()
usecase_router = routers.DefaultRouter()

# Classes
class_router.register('class', ClassViewSet, basename='class')
class_router.register('class_attribute_enum', ClassAttributeEnumViewSet, basename='class_attribute_enum')
class_router.register('class_attribute_prim', ClassAttributePrimViewSet, basename='class_attribute_prim')
class_router.register('enum', EnumViewSet, basename='enum')
class_router.register('enum_attribute', EnumAttributeViewSet, basename='enum_attribute')
class_router.register('relation', RelationViewSet, basename='relation')
class_router.register('relation_class_reference', RelationClassReferenceViewSet, basename='relation_class_reference')

# Use Case
usecase_router.register('actor', ActorViewSet, basename='actor')
usecase_router.register('event', EventViewSet, basename='event')
usecase_router.register('step', StepViewSet, basename='step')
usecase_router.register('usecase', UsecaseViewSet, basename='usecase')

urlpatterns = [
   path("", schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path("classes/", include(class_router.urls)),
   path("use_cases/", include(usecase_router.urls))
]