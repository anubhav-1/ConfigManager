from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate


class Login(APIView):


    def post(self, request):
        user = request.data.get('username')
        password = request.data.get('password')
        auth_obj = authenticate(username=user, password=password)
        if auth_obj:
            user_obj = User.objects.get(username=user)
            token = Token.objects.get_or_create(user=user_obj)
            response = {'User': user,
                       'Token': token[0].key}
            return Response(data=response, status= HTTP_200_OK)
        return Response(status=HTTP_400_BAD_REQUEST, data="User Does Not Exist")