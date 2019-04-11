from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .serializers import UserSerializer, GroupSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
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
    permission_classes = (IsAuthenticated,)

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
    permission_classes = (IsAuthenticated,)

    serializer_class = DoctorSerializer
    def get_queryset(self, *args, **kwargs):
        queryset_list = Doctor.objects.all()
        query = self.request.GET.get("q")
        if query:
            queryset_list = queryset_list.filter(
            Q(nombre__icontains=query)
            ).distinct()
        return queryset_list


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
