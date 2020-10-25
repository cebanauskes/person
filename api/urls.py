from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.decorators import action

from .views import PersonViewSet, compare

router = DefaultRouter()

router.register('persons', PersonViewSet, basename='person')

urlpatterns = [
    path('', include(router.urls)),
    path('persons/compare/<uuid:pk_1>&<uuid:pk_2>/', compare)
]