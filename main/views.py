from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.viewsets import ModelViewSet

from .models import *
from .serializers import ProblemaSerializer


# class ProblemListView(ListAPIView):    # нам нужны список всех проблем
#     queryset = Problema.objects.all()
#     serializer_class = ProblemaSerializer     # берет данные и форматирует в формат json
#
#
# class ProblemaDetailView(RetrieveAPIView):
#     queryset = Problema.objects.all()
#     serializer_class = ProblemaSerializer
#
#
# class ProblemCreateView(CreateAPIView):
#     queryset = Problema.objects.all()
#     serializer_class = ProblemaSerializer
#
#     def get_serializer_context(self):
#         return {'request': self.request}
#
#
# class ProblemUpdateView(UpdateAPIView):
#     queryset = Problema.objects.all()
#     serializer_class = ProblemaSerializer
#
#     def get_serializer_context(self):
#         return {'request': self.request}
#
#
# class ProblemDeleteView(DestroyAPIView):
#     queryset = Problema.objects.all()
#     serializer_class = ProblemaSerializer
#

class ProblemViewSet(ModelViewSet):
    queryset = Problema.objects.all()
    serializer_class = ProblemaSerializer

    def get_serializer_context(self):
        return {'request': self.request}