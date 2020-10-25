import math

import numpy as np
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from scipy.spatial import distance

from .models import Person
from .serializers import (
    PersonIdSerializer,
    PersonCreateSerializer,
    GetPersonSerializer
)
from .utils import get_vector


class PersonViewSet(viewsets.ViewSet):

    def list(self, request):
        """Выводит ID вех экземпляров Person"""
        queryset = Person.objects.all()
        serializer = PersonIdSerializer(queryset, many=True)

        return Response(serializer.data)

    def create(self, request):
        """Создает экземпляр Person с first_name и last_name."""
        serializer = PersonCreateSerializer(data=request.data)

        if serializer.is_valid():
            person = Person.objects.create(**serializer.validated_data)

            return Response(
                {'id': person.pk}, status=status.HTTP_201_CREATED
            )

        return Response(status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk):
        """Выводит ия и фамилию одного экземпляра Person."""
        queryset = get_object_or_404(Person, pk=pk)
        serializer = GetPersonSerializer(queryset)

        return Response(serializer.data)

    def update(self, request, pk):
        """Добавляет вектор к экземпляру Person."""
        size = (300, 300)                       # размер, до которого нужно сжать изображение
        vector = get_vector(request, size)      # получает вектор из запроса
        serializer = PersonCreateSerializer(data=request.data)

        if serializer.is_valid():
            Person.objects.filter(pk=pk).update(
                **serializer.validated_data,
                vector=vector, have_vector=True
            )

            return Response(status=status.HTTP_200_OK)

        return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        """Удаляет экземпляр Person."""
        obj = Person.objects.filter(pk=pk).delete()

        if obj[0] > 0:

            return Response(
                status=status.HTTP_204_NO_CONTENT
            )

        else:

            return Response(
                status=status.HTTP_400_BAD_REQUEST
            )


@api_view()
def compare(request, pk_1, pk_2):
    """Находит евклидово расстояние
    между векторами двух экземпляров Person.
    
    """
    vector1 = get_object_or_404(Person, pk=pk_1).vector
    vector2 = get_object_or_404(Person, pk=pk_2).vector
    vector1 = vector1[1:-1].split(', ')
    vector2 = vector2[1:-1].split(', ')

    for i in range(len(vector1)):
        vector1[i] = float(vector1[i])

    for i in range(len(vector2)):
        vector2[i] = float(vector2[i])
    
    result = math.sqrt(
        sum([(a - b) ** 2 for a, b in zip(vector1, vector2)])
    )
    
    return Response({'result': result})
