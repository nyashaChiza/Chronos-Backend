from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from allauth.account import views as allauth_views
from rest_framework.decorators import api_view

class RegisterAPIView(APIView):
    def post(self, request):
        # Call the Allauth RegistrationView to handle user registration
        view = allauth_views.RegistrationView.as_view()
        response = view(request)
        return Response(response.data, status=response.status_code)

class LoginAPIView(APIView):
    def post(self, request):
        # Call the Allauth LoginView to handle user login
        view = allauth_views.LoginView.as_view()
        response = view(request)
        return Response(response.data, status=response.status_code)

class LogoutAPIView(APIView):
    def post(self, request):
        # Call the Allauth LogoutView to handle user logout
        view = allauth_views.LogoutView.as_view()
        response = view(request)
        return Response(response.data, status=response.status_code)