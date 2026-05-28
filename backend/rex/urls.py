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

import rex.views.class_view as cls_viw
import rex.views.usecase_view as uc_viw
from rex.views.ai_view import AiViewSet
from rex.views.generator_view import JsonGeneratorViewSet

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
ai_router = routers.DefaultRouter()
generator_router = routers.DefaultRouter()

# AI
ai_router.register('ai', AiViewSet, basename='ai')

# Generator
generator_router.register('json', JsonGeneratorViewSet, basename='json')

# Classes
class_router.register('class', cls_viw.ClassViewSet, basename='class')
class_router.register('class_attribute_enum', cls_viw.ClassAttributeEnumViewSet, basename='class_attribute_enum')
class_router.register('class_attribute_prim', cls_viw.ClassAttributePrimViewSet, basename='class_attribute_prim')
class_router.register('enum', cls_viw.EnumViewSet, basename='enum')
class_router.register('enum_attribute', cls_viw.EnumAttributeViewSet, basename='enum_attribute')
class_router.register('relation', cls_viw.RelationViewSet, basename='relation')
class_router.register('relation_class_reference', cls_viw.RelationClassReferenceViewSet, basename='relation_class_reference')
class_router.register('inheritance', cls_viw.InheritanceViewSet, basename='inheritance')

# Use Case
usecase_router.register('actor', uc_viw.ActorViewSet, basename='actor')
usecase_router.register('event', uc_viw.EventViewSet, basename='event')
usecase_router.register('step', uc_viw.StepViewSet, basename='step')
usecase_router.register('action', uc_viw.ActionViewSet, basename='action')
usecase_router.register('modify_action', uc_viw.ModifyActionViewSet, basename='modify_action')
usecase_router.register('read_action', uc_viw.ReadActionViewSet, basename='read_action')
usecase_router.register('text_read_action', uc_viw.TextReadActionViewSet, basename='text_read_action')
usecase_router.register('decision', uc_viw.DecisionViewSet, basename='decision')
usecase_router.register('usecase', uc_viw.UsecaseViewSet, basename='usecase')

urlpatterns = [
   path("", schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path("classes/", include(class_router.urls)),
   path("usecases/", include(usecase_router.urls)),
   path("", include(ai_router.urls)),
   path("", include(generator_router.urls))
]