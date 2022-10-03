from django.shortcuts import render
# from rest_framework.decorators import api_view
# from django.http import HttpResponse, HttpResponseRedirect
# from django.http import JsonResponse, HttpResponseForbidden, HttpResponseBadRequest
# import requests
# from rest_framework.response import Response
# from .login_config import config
# from . import models
# from django.contrib.auth import login, logout
# from rest_framework import viewsets
# from .serializers import MemberSerializer
#
# from rest_framework.decorators import action
# from rest_framework.permissions import IsAuthenticated, AllowAny
# from rest_framework import status
#
#
# @api_view(['GET'])
# def check(request):
#     msg = {
#         "loggedin": False
#     }
#     if request.user.is_authenticated:
#         msg["loggedin"] = True
#         res = Response(msg, status=status.HTTP_202_ACCEPTED)
#         res['Access-Control-Allow-Origin'] = 'http://127.0.0.1:8000'
#         res['Access-Control-Allow-Credentials'] = 'true'
#         return res
#     else:
#         res = Response(msg, status=status.HTTP_202_ACCEPTED)
#         res['Access-Control-Allow-Origin'] = 'http://127.0.0.1:8000'
#         res['Access-Control-Allow-Credentials'] = 'true'
#         return res
#
#
# class LoginViewSet(viewsets.ModelViewSet):
#     queryset = models.Member
#     serializer_class = MemberSerializer
#
#     @action(detail=False, url_path='login', url_name='login-login')
#     def login1(self):
#         print("login1")
#         url = f"https://channeli.in/oauth/authorise/?client_id={config['CLIENT_ID']}&redirect_uri={config['REDIRECT_URI']}&state={config['STATE_STRING']}"
#         return HttpResponseRedirect(url)
#
#     @action(detail=False, url_path='OAuth', url_name='login-OAuth')
#     def login2(self, req):
#         try:
#             auth_code = self.request.query_params.get('code')
#         except:
#             return HttpResponseBadRequest()
#
#         params = {
#             'client_id': config['CLIENT_ID'],
#             'client_secret': config['CLIENT_SECRET'],
#             'grant_type': 'authorization_code',
#             'redirect_uri': config['REDIRECT_URI'],
#             'code': auth_code,
#         }
#
#         res = requests.post("https://channeli.in/open_auth/token/", data=params)
#
#         if res.status_code == 200:
#             access_token = res.json()['access_token']
#             refresh_token = res.json()['refresh_token']
#         else:
#             return HttpResponseBadRequest()
#
#         header = {
#             "Authorization": "Bearer " + access_token,
#         }
#
#         res1 = requests.get("https://channeli.in/open_auth/get_user_data/", headers=header)
#         data_final = res1.json()
#
#         isMaintainer = False
#         active = True
#         for role in data_final['person']['roles']:
#             if role['role'] == 'Maintainer':
#                 isMaintainer = True
#
#         print(data_final)
#         if not isMaintainer:
#             return JsonResponse({'status': 'you are not a maintainer'})
#
#         try:
#             user = models.Member
#
#         except:
#             print("saving data")
#             username = data_final['username']
#             user_name = data_final['person']['fullName']
#             email_id = data_final['contactInformation']['emailAddress']
#             ern = data_final['username']
#             isAdmin = False
#             isEnabled = True
#             profile_url = data_final['person']['displayPicture']
#             user = models.Applicant(enrollment_no=ern, User_name=user_name, admin=isAdmin, enabled=isEnabled, email=email_id,
#                                  profile=profile_url, username=username)
#
#             print("saving")
#             user.save()
#             print("saved")
#         login(request=req, user=user)
#         info = {
#             'data': 'Done!',
#         }
#         res = Response(info, status=status.HTTP_202_ACCEPTED)
#         res['Access-Control-Allow-Origin'] = 'http://127.0.0.1:3000'
#         res['Access-Control-Allow-Credentials'] = 'true'
#         return res
#
#     @action(methods=['GET'], detail=False, url_path='logout', url_name='login-logout')
#     def logout_(self, request):
#         if request.user.is_authenticated:
#             logout(request)
#             res = Response({'status': 'successful'}, status=status.HTTP_202_ACCEPTED)
#             res['Access-Control-Allow-Origin'] = 'http://127.0.0.1:3000'
#             res['Access-Control-Allow-Credentials'] = 'true'
#             return res
#         else:
#             return HttpResponseForbidden()


from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *
from rest_framework.permissions import *
from .permissions import *


class RecruitmentSeasonViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = RecruitmentSeason.objects.all()
    serializer_class = RecruitmentSeasonSerializer


class TestViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = RecruitmentSeason.objects.all()
    serializer_class = TestSerializer


class QuestionViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = RecruitmentSeason.objects.all()
    serializer_class = QuestionSerializer


class AnswerViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = RecruitmentSeason.objects.all()
    serializer_class = AnswerSerializer


class InterviewViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = RecruitmentSeason.objects.all()
    serializer_class = InterviewSerializer


class InterviewPanelViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = RecruitmentSeason.objects.all()
    serializer_class = InterviewPanelSerializer


class MemberViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = RecruitmentSeason.objects.all()
    serializer_class = MemberSerializer


class ApplicantViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = RecruitmentSeason.objects.all()
    serializer_class = ApplicantSerializer


class ScoreViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = RecruitmentSeason.objects.all()
    serializer_class = ScoreSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = RecruitmentSeason.objects.all()
    serializer_class = ProjectSerializer


class SectionViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = RecruitmentSeason.objects.all()
    serializer_class = SectionSerializer


class RoundViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = RecruitmentSeason.objects.all()
    serializer_class = RoundSerializer
