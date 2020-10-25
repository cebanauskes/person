from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.decorators import action

from .views import PersonViewSet, compare

router = DefaultRouter()

router.register('persons', PersonViewSet, basename='person')
# from .views import (
#     CreatePersonView,
#     # ListAllPersonsView,
#     GetPersonView,
#     DeletePersonView,
# )

urlpatterns = [
    path('', include(router.urls)),
    path('persons/compare/<uuid:pk_1>&<uuid:pk_2>', compare)
    # path('persons/', CreatePersonView.as_view(), name='create_person'),
    # # path('persons/', ListAllPersonsView.as_view(), name='list_all_persons'),
    # path('persons/<str:person_id>', GetPersonView.as_view(), name='get_person'),
    # path('persons/<str:person_id>', DeletePersonView.as_view(), name='delete_person'),
]