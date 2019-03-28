from rest_framework import generics
from .models import Doctor
from .serializers import DoctorSerializer
from django.db.models import Q
from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    ListAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView
    )


class doctorCedulaSearch(ListAPIView):
    serializer_class = DoctorSerializer
    def get_queryset(self, *args, **kwargs):
        queryset_list = Doctor.objects.all()
        query = self.request.GET.get("q")
        if query:
            queryset_list = queryset_list.filter(
            Q(cedula__icontains=query)
            ).distinct()
        return queryset_list




class doctorNombreSearch(ListAPIView):
    serializer_class = DoctorSerializer
    def get_queryset(self, *args, **kwargs):
        queryset_list = Doctor.objects.all()
        query = self.request.GET.get("q")
        if query:
            queryset_list = queryset_list.filter(
            Q(nombre__icontains=query)
            ).distinct()
        return queryset_list


