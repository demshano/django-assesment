from django.db import models

# Create your models here.

class School(models.Model):
    id = models.CharField(max_length=50)
    name = models.CharField(max_length=100)

class Class(models.Model):
    id = models.CharField(max_length=50)
    name = models.CharField(max_length=100)

class Assessment_ares(models.Model):
    id = models.CharField(max_length=50)
    name = models.CharField(max_length=100)

class Student(models.Model):
    id = models.CharField(max_length=50)
    full_name = models.CharField(max_length=100)
     
class Answers(models.Model):
    id = models.CharField(max_length=50)
    answers = models.CharField(max_length=100)

class Summary(models.Model):
    School_ID = models.CharField(max_length=50)
    Sydney_Participant = models.CharField(max_length=100, null=True, blank=True)
    Sydney_Percentile = models.FloatField(max_length=100, null=True, blank=True)
    Assessment_Area_Id = models.CharField(max_length=50, null=True, blank=True)
    Award_Id = models.CharField(max_length=50, null=True, blank=True)
    Class_Id = models.CharField(max_length=50, null=True, blank=True)
    Corret_answer_percentage_per_class = models.FloatField(null=True, blank=True)
    Correct_Answer = models.CharField(max_length=255, null=True, blank=True)
    Student_Id = models.CharField(max_length=50, null=True, blank=True)
    Participant = models.CharField(max_length=255, null=True, blank=True)
    Student_score = models.FloatField(null=True, blank=True)
    Subject_Id = models.CharField(max_length=50, null=True, blank=True)
    Category_Id = models.CharField(max_length=50, null=True, blank=True)
    Year_level_name = models.CharField(max_length=100, null=True, blank=True)
    Answer_Id = models.CharField(max_length=50, null=True, blank=True)
    Correct_answer_Id = models.CharField(max_length=50, null=True, blank=True)

class Awards(models.Model):
    id = models.CharField(max_length=50)
    name = models.CharField(max_length=100)

class Subject(models.Model):
    id = models.CharField(max_length=50)
    subject = models.CharField(max_length=100)
    subject_score = models.FloatField(max_length=100)