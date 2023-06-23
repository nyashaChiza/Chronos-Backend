# from django.contrib.auth.models import User
# from django.test import TestCase, RequestFactory
# from rest_framework import status
# from allauth.account import views as allauth_views
# from django.contrib.messages.storage.fallback import FallbackStorage

# class RegisterLoginLogoutTest(TestCase):
#     def setUp(self):
#         self.factory = RequestFactory()
#         self.user = User.objects.create_user(username='testuser', password='testpassword')

#     def test_register_view(self):
#         request = self.factory.post('/register/')
#         request.session = self.client.session
#         response = allauth_views.signup(request)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)

#     def test_login_view(self):
#         request = self.factory.post('/login/')
#         request.session = self.client.session
#         response = allauth_views.login(request)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)

#     def test_logout_view(self):
#         request = self.factory.post('/logout/')
#         request.user = self.user
#         request.session = self.client.session
#         response = allauth_views.logout(request)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)