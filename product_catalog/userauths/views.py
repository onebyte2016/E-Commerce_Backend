from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import RetrieveUpdateAPIView, CreateAPIView
from .serializers import CustomUserSerializer, LoginUserSerializer, RegisterUserSerializer
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken, TokenError
from rest_framework.response import Response
from rest_framework import status 
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework_simplejwt.exceptions import InvalidToken
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

# Create your views here.
class CustomUserView(RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CustomUserSerializer

    def get_object(self):
        return self.request.user

class UserRegistrationView(CreateAPIView):
    serializer_class = RegisterUserSerializer


class LoginView(APIView):
    @swagger_auto_schema(
    request_body=LoginUserSerializer,
    responses={200: CustomUserSerializer}
    )
    def post(self, request):
        serializer = LoginUserSerializer(data=request.data)

        if serializer.is_valid():
            user = serializer.validated_data
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)

            response = Response({"user":CustomUserSerializer(user).data},
                                status=status.HTTP_200_OK)
            response.set_cookie(key="access_token", 
                                value=access_token, 
                                httponly=True, 
                                secure=True, 
                                samesite="None")
            
            response.set_cookie(key="refresh_token", 
                                value=str(refresh), 
                                httponly=True, 
                                secure=True, 
                                samesite="Strict")
            return response
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LogoutView(APIView):
    def post(self, request):
        refresh_token = request.COOKIES.get("refresh_token")  # fixed spelling

        if refresh_token is None:
            return Response({"error": "No refresh token found"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            token = RefreshToken(refresh_token)
            token.blacklist()  # blacklist the refresh token
        except TokenError:
            return Response({"error": "Invalid or expired refresh token"}, status=status.HTTP_400_BAD_REQUEST)

        response = Response({"message": "Successfully logged out"}, status=status.HTTP_200_OK)
        # clear cookies
        response.delete_cookie("access_token")
        response.delete_cookie("refresh_token")
        return response


# class LogoutView(APIView):
#     def post(self, request):
#         refresh_token = request.COOKIES.get("refresh_token")

#         if refresh_token:
#             try:
#                 refresh = RefreshToken(refresh_token)
#                 refresh_token.blacklist()
#             except Exception as e:
#                 return Response({"error":"Error invalidating token:" + str()}, status=status.HTTP_400_BAD_REQUEST)
#             response = Response({"message": "Successfully logged out!"}, status=status.HTTP_200_OK)
#             response.delete_cookie("access_token")
#             response.delete_cookie("refresh_token")
#             return response

class CookieTokenRefreshView(TokenRefreshView):
    def post(self, request):
        refresh_token = request.COOKIES.get("refresh_token")

        if not refresh_token:
            return Response({"error": "Refresh token not provided"}, status=status.HTTP_401_UNAUTHORIZED)
        try:
            refresh = RefreshToken(refresh_token)
            access_token = str(refresh.access_token)

            response = Response({"Message": "Access token refreshed successfully"}, status=status.HTTP_200_OK)
            response.set_cookie(key="access_token", 
                                value=access_token, 
                                 httponly=True, 
                                 secure=True, 
                                 samesite="Strict")
            return response
        except InvalidToken:
            return Response({"error": "Invalid token"}, status=status.HTTP_401_UNAUTHORIZED)