# from django.contrib import admin
# from django.contrib.messages import success
# from django.db import router

from rest_framework.routers import DefaultRouter
from .views import *
from django.urls import path, include

router=DefaultRouter()

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

urlpatterns = [path('', include(router.urls)), ]