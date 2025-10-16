from rest_framework import serializers
from .models import Pet, Owner


class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Owner
        fields = ["id", "nombre", "telefono"]


class PetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        fields = ["id", "nombre", "especie", "edad", "dueño"]


class PetDetailSerializer(serializers.ModelSerializer):
    dueño = OwnerSerializer(read_only=True)

    class Meta:
        model = Pet
        fields = ["id", "nombre", "especie", "edad", "dueño"]
