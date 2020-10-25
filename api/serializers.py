from rest_framework import serializers

from .models import Person


class PersonIdSerializer(serializers.ModelSerializer):

    class Meta:
        model = Person
        fields = (
            'id',
        )


class PersonCreateUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Person
        fields = (
            'id',
            'first_name',
            'last_name',
        )

    
class GetPersonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Person
        fields = (
            'first_name',
            'last_name',
            'have_vector',
        )