from django.shortcuts import render, get_object_or_404

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import Company
from .serializers import CompanySerializer

# Create your views here.
class CompanyViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def list(self, request):
        queryset = Company.objects.all()
        serializer = CompanySerializer(queryset, many=True, context={'request': request})
        response_dict = {
            "error": False,
            "message": "All Company List Data.",
            "data": serializer.data
        }
        return Response(response_dict)

    def create(self, request):
        serializer = CompanySerializer(data=request.data, context={'request': request})
        try:
            serializer.is_valid()
            serializer.save()
            response_dict = {
                "error": False,
                "message": "Company Data Saved Successfully.",
            }
        except:
            response_dict = {
                "error": True,
                "message": "Error During Saving Company Data.",
            }
        return  Response(response_dict)

    def update(self, request, pk=None):
        try:
            queryset = Company.objects.all()
            company = get_object_or_404(queryset, pk=pk)
            serializer = CompanySerializer(company, data=request.data, context={'request': request})
            serializer.is_valid()
            serializer.save()
            response_dict = {
                "error": False,
                "message": "Company Data Updated Successfully.",
            }
            
        except:
            response_dict = {
                "error": True,
                "message": "Error During Updating Company Data.",
            }
        return Response(response_dict)




company_list = CompanyViewSet.as_view({"get": "list"})
company_create = CompanyViewSet.as_view({"post": "create"})
company_update = CompanyViewSet.as_view({"put": "update"}) 