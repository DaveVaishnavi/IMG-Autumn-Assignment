from .serializers import *
from rest_framework import viewsets
from rest_framework.decorators import action
import csv
import codecs
from .models import Member
from django.shortcuts import redirect
from rest_framework.response import Response
import requests
from django.contrib.auth import login, logout
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from .serializers import MemberSerializer
from rest_framework import status


CLIENT_ID = "qxzf6ez39LBvOF6w9ghzvstlLXX3oiQRV35eqfW8"
CLIENT_SECRET = "jC5qtSsDwgtXNZqkeuDeDuMroOixWXf1uTFIsQ9Qr3BfeqNzNS22jOooap4g7jrTVxaMVm41Mrf1lqYTmNR0SwyDiGCBBEXoMCM0FPcXeRBTik0vVRKB1LNMQoXEISH7"


class RecruitmentSeasonViewSet(viewsets.ModelViewSet):
    queryset = RecruitmentSeason.objects.all()
    serializer_class = RecruitmentSeasonSerializer

    def dispatch(self, *args, **kwargs):
        res = super(RecruitmentSeasonViewSet, self).dispatch(*args, **kwargs)
        res['Access-Control-Allow-Origin'] = 'http://localhost:3000'
        res['Access-Control-Allow-Credentials'] = 'true'
        return res

    # def list(self, request, pk=None):
    #     print("Abs")
    #     # res = super(RecruitmentSeasonViewSet, self).dispatch(*args, **kwargs)
    #     res = Response("done", status=status.HTTP_202_ACCEPTED)
    #     res['Access-Control-Allow-Origin'] = 'http://localhost:3000'
    #     res['Access-Control-Allow-Credentials'] = 'true'
    #     return res


class TestViewSet(viewsets.ModelViewSet):
    queryset = Test.objects.all()
    serializer_class = TestSerializer


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer


class InterviewViewSet(viewsets.ModelViewSet):
    queryset = Interview.objects.all()
    serializer_class = InterviewSerializer


class InterviewPanelViewSet(viewsets.ModelViewSet):
    queryset = InterviewPanel.objects.all()
    serializer_class = InterviewPanelSerializer


class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer


class ScoreViewSet(viewsets.ModelViewSet):
    queryset = Score.objects.all()
    serializer_class = ScoreSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class SectionViewSet(viewsets.ModelViewSet):
    queryset = Section.objects.all()
    serializer_class = SectionSerializer


class RoundViewSet(viewsets.ModelViewSet):
    queryset = Round.objects.all()
    serializer_class = RoundSerializer


def auth(username, name, year, email, enrolment_number):
    try:
        user = Member.objects.get(username=username)
        return user
    except Member.DoesNotExist:
        Member.objects.create(username=username, name=name, email=email,
                              year_of_study=year, enroll_no=enrolment_number)
        user = Member.objects.get(username=username)
        if year >= 3:
            user.FullAccessPermission = True
        return user


def get_user(username):
    try:
        return Member.objects.get(username=username)
    except Member.DoesNotExist:
        return None


@api_view(('GET',))
@permission_classes([])
def check_login(request):
    print(request.__dict__)
    content = {'Logged_In': False}
    if request.user.is_authenticated:
        serializer = MemberSerializer(request.user)
        content = {'Logged_In': True, 'user': serializer.data}

    return Response(content)


@api_view(('GET',))
@authentication_classes([])
@permission_classes([])
def login_redirect(request):
    SITE = f'https://channeli.in/oauth/authorise/?client_id={CLIENT_ID}&redirect_uri=http://localhost:8000/get_oauth_token/'
    return redirect(SITE)


@api_view(('GET', 'POST'))
@authentication_classes([])
@permission_classes([])
def get_token(request):
    print("here1")
    AUTHORISATION_CODE = request.query_params.get('code', '')

    print("auth code: ", AUTHORISATION_CODE)

    post_data = {
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "grant_type": "authorization_code",
        "redirect_uri": "http://localhost:3000/intermediate_page/",
        "code": AUTHORISATION_CODE,
    }

    response = requests.post('https://channeli.in/open_auth/token/', post_data)

    ACCESS_TOKEN = response.json().get('access_token', '')
    TOKEN_TYPE = response.json().get('token_type', '')
    REFRESH_TOKEN = response.json().get('refresh_token', '')

    authorization_data = {
        "Authorization": f"{TOKEN_TYPE} {ACCESS_TOKEN}"
    }

    response = requests.get(
        'https://channeli.in/open_auth/get_user_data/', headers=authorization_data)

    is_member = False
    name = response.json()['person']['fullName']
    username = response.json()['username']
    year_of_study = response.json()['student']['currentYear']
    email = response.json()['contactInformation']['emailAddress']
    enroll_no = response.json()['student']['enrolmentNumber']

    for role in response.json()['person']['roles']:
        if role['role'] == "Maintainer":
            is_member = True

    if is_member:
        try:
            user = auth(username=username, name=name, year=year_of_study,
                        email=email, enrolment_number=enroll_no)
        except:
            return Response("unable to create user")
        try:
            login(request, user)
        except:
            return Response("unable to log in successfully")
    else:
        return Response("You are not a member of IMG")

    print(user)
    # return redirect('http://localhost:3000/dashboard')
    res = Response("done", status=status.HTTP_202_ACCEPTED)
    res['Access-Control-Allow-Origin'] = 'http://localhost:3000'
    res['Access-Control-Allow-Credentials'] = 'true'
    return res


@api_view(('GET',))
def logout_user(request):
    if request.user.is_authenticated:
        logout(request)
        return Response("user logged out Successfully")


class ApplicantViewSet(viewsets.ModelViewSet):
    queryset = Applicant.objects.all()
    serializer_class = ApplicantSerializer

    @action(detail=False, methods=['POST'])
    def upload_data_through_file(self, request):
        file = request.FILES.get("file")
        season_id = request.POST.get("season_id")

        reader = csv.DictReader(codecs.iterdecode(file, "utf-8"), delimiter=",")
        data = list(reader)

        serializer = self.serializer_class(data=data, many=True)
        serializer.is_valid(raise_exception=True)

        applicant_list = []
        for row in serializer.data:
            applicant_list.append(
                Applicant(
                    name=row['name'],
                    email=row['email'],
                    mobile_no=row['mobile_no'],
                    branch=row['branch'],
                    year_of_study=row['year'],
                    cgpa=row['CG'],
                    enroll_no=row['enrolment_number'],
                    season_id=season_id,
                )
            )
        Applicant.objects.bulk_create(applicant_list)
        return Response("candidates registered successfully")
