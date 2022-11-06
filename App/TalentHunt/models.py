from django.contrib.auth.models import AbstractUser
from django.db import models


class RecruitmentSeason(models.Model):
    year_of_season = models.IntegerField()
    no_of_rounds = models.IntegerField()
    season_name = models.CharField(max_length=255)


class Test(models.Model):
    no_of_sections = models.IntegerField()
    season = models.OneToOneField(RecruitmentSeason, on_delete=models.CASCADE)


class Round(models.Model):
    type = models.CharField(max_length=255)


class Applicant(models.Model):
    DoesNotExist = None
    season = models.ForeignKey(RecruitmentSeason, on_delete=models.CASCADE)
    round = models.ForeignKey(Round, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    branch = models.CharField(max_length=255)
    stage = models.CharField(max_length=255)
    enroll_no = models.IntegerField()
    years_of_study = (
        ("1", "1"),
        ("2", "2"),
        ("3", "3"),
        ("4", "4"),
    )
    year_of_study = models.CharField(max_length=1, choices=years_of_study)
    cgpa = models.IntegerField()
    total_score = models.IntegerField()


class Member(AbstractUser):
    username = models.CharField(max_length=255, unique=True, primary_key=True)
    email = models.EmailField(max_length=255, null=True)
    years_of_study = (
        ("1", "1"),
        ("2", "2"),
        ("3", "3"),
        ("4", "4"),
    )
    year_of_study = models.CharField(max_length=1, choices=years_of_study)
    role_choices = (
        ("Developer", "Developer"),
        ("Designer", "Designer"),
    )
    role = models.CharField(max_length=255, choices=role_choices)
    name = models.CharField(max_length=255, default="")
    branch = models.CharField(max_length=255, null=True)
    enroll_no = models.IntegerField()
    USERNAME_FIELD = 'username'


class Section(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    max_marks = models.IntegerField()
    weight = models.IntegerField()


class Score(models.Model):
    applicant = models.OneToOneField(Applicant, on_delete=models.CASCADE)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    remarks = models.TextField()
    scored_marks = models.IntegerField()


class Question(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    # maker = models.ForeignKey(Member, on_delete=models.CASCADE)
    question_text = models.TextField()
    max_marks = models.IntegerField()
    assignee = models.ManyToManyField(Member)


class Project(models.Model):
    applicant = models.ForeignKey(Applicant, on_delete=models.CASCADE)
    remarks = models.TextField()
    marks = models.IntegerField()


class InterviewPanel(models.Model):
    member = models.ManyToManyField(Member)
    applicant = models.ForeignKey(Applicant, on_delete=models.CASCADE)
    place = models.CharField(max_length=255)
    status_choices = (
        ("Interviewing", "Interviewing"),
        ("Disabled", "Disabled"),
        ("Idle", "Idle"),
    )
    status = models.CharField(max_length=255, choices=status_choices)
    interview_choices = (
        ("Tech Dev", "Tech Dev"),
        ("Tech Design", "Tech Design"),
        ("HR Tech", "HR Tech"),
        ("HR Design", "HR Design"),
    )
    type = models.CharField(max_length=255, choices=interview_choices)


class Interview(models.Model):
    interview_panel = models.ForeignKey(InterviewPanel, on_delete=models.CASCADE)
    applicant = models.ForeignKey(Applicant, on_delete=models.CASCADE)
    time_of_interview = models.DateTimeField()
    call_remarks = models.TextField()
    call_status_choices = (
        ("Called and Confirmed", "Called and Confirmed"),
        ("Called but not confirmed", "Called but not confirmed"),
        ("Not called", "Not called"),
    )
    call_status = models.TextField(max_length=255, choices=call_status_choices)
    round = models.ForeignKey(Round, on_delete=models.CASCADE)


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    awarded_marks = models.IntegerField()
    answer_text = models.TextField()
    applicant = models.ForeignKey(Applicant, on_delete=models.CASCADE)
    remarks = models.TextField()
    status_choices = (
        ("Checked", "Checked"),
        ("Unchecked", "Unchecked"),
    )
    check_status = models.CharField(max_length=255, choices=status_choices)

