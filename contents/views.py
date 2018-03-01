import json

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status,viewsets,parsers,views,permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from rest_framework.renderers import JSONRenderer
from contents.models import userAdmin, userProfile
from contents.serializers import userAdminSerializer, userProfileSerializer



@csrf_exempt
@api_view(['GET'])
def adminAccount(request):
    if request.method =='GET':
        accounts = userAdmin.objects.all()
        serializer = userAdminSerializer(accounts,many = True)
        return Response(serializer.data)

#@csrf_exempt
class userProfileView(APIView):
    #parser_classes = (MultiPartParser, FormParser,)

    def get(self, request, format=None):
        profile = userProfile.objects.all()
        serializer = userProfileSerializer(profile, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
       serializer = userProfileSerializer(data=request.data)
       if serializer.is_valid():
           serializer.save()
           return Response(serializer.data, status=status.HTTP_201_CREATED)
       return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class userProfileViewSet(viewsets.ModelViewSet):
#     queryset = userProfile.objects.all()
#     serializer_class = userProfileSerializer

#     def get_permissions(self):
#         if self.request.method in permissions.SAFE_METHODS:
#             return (permissions.AllowAny(),)
#         if self.request.method == 'POST':
#             return (permissions.AllowAny(),)

#         return (permissions.IsAuthenticated(),)

#     def create(self, request):
#         serializer = self.serializer_class(data=request.data)
#         if serializer.is_valid():
#             userProfile.objects.create_user(**serializer.validated_data)

#             return Response(serializer.validated_data, status=status.HTTP_201_CREATED)
#         return JSONResponse(serializer.errors, status=400)
# # @csrf_exempt
# # @api_view(['GET','POST','PUT'])
# # def patientProfile(request):
# #     if request.method == 'GET':
# #         patients = userProfile.objects.all()
# #         serializer = userProfileSerializer(patients,many = True)
# #         return Response(serializer.data)
# #     elif request.method == 'POST':
# #         serializer = userProfileSerializer(data=request.data)
# #         if serializer.is_valid():
# #             m = userProfile.object.get(pk=course_id)
# #             m.eye = form.cleaned_data['image']
# #             m.face = form.cleaned_data['image']
# #             m.save()
# #             return Response(serializer.data, status=status.HTTP_201_CREATED)
# #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# # def upload_pic(request):
# #     if request.method == 'POST':
# #         form = ImageUploadForm(request.POST, request.FILES)
# #         if form.is_valid():
# #             m = ExampleModel.objects.get(pk=course_id)
# #             m.model_pic = form.cleaned_data['image']
# #             m.save()
# #             return HttpResponse('image upload success')
# #     return HttpResponseForbidden('allowed only via POST')

# # class ExampleModelViewSet(viewsets.ModelViewSet):
# #     queryset = ExampleModel.objects.all()
# #     serializer_class = ExampleModelSerializer

# # Create your views here.
# # class userProfileViewSet(viewsets.ModelViewSet):
# #     queryset = userProfile.objects.all()
# #     serializer_class = userProfileSerializer