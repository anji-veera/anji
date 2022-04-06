from django.shortcuts import render
from .models import Student
from .serializers import *
from rest_framework.generics  import GenericAPIView
from rest_framework.mixins import *

# Create your views here.
class Studentlist(GenericAPIView,ListModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    def get(self,request):
        return self.list(request)

class Studentcreate(GenericAPIView,CreateModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    def post(self,request):
        return self.create(request)

class Studentdis(GenericAPIView,RetrieveModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    def get(self,request,**kwargs):
        return self.retrieve(request,**kwargs)

class Studentupdate(GenericAPIView,UpdateModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    def put(self,request,**kwargs):
        return self.update(request,**kwargs)

class Studentdelete(GenericAPIView,DestroyModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    def delete(self,request,**kwargs):
        return self.destroy(request,**kwargs)