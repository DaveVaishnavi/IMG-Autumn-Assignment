from rest_framework import routers
from .views import *
from django.urls import path, include

router = routers.SimpleRouter()
router.register('season', RecruitmentSeasonViewSet)
router.register('applicant', ApplicantViewSet)
router.register('member', MemberViewSet)
router.register('test', TestViewSet)
router.register('section', SectionViewSet)
router.register('question', QuestionViewSet)
router.register('answer', AnswerViewSet)
router.register('interview', InterviewViewSet)
router.register('interview_panel', InterviewPanelViewSet)
router.register('project', ProjectViewSet)
router.register('round', RoundViewSet)
router.register('score', ScoreViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('get_token/', get_token),
    # path('send_token_request/', login_redirect),
    path('logout/', logout_user),
    path('check_login/', check_login)
]

