from rest_framework import viewsets, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from .models import Pet, Owner
from .serializers import PetSerializer, PetDetailSerializer, OwnerSerializer


class PetViewSet(viewsets.ModelViewSet):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ["especie", "edad"]
    search_fields = ["nombre", "especie"]

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = PetDetailSerializer(instance)
        return Response(serializer.data)

    @action(detail=False, methods=["get"])
    def search(self, request):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class OwnerViewSet(viewsets.ModelViewSet):
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer
