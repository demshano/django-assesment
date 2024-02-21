from django.contrib import admin
from django.urls import path
from django.shortcuts import render
from .models import School, Class, AssessmentArea, Student, Answers, Summary, Awards, Subject
from django import forms

class CsvImportForm(forms.Form):
    csv_upload = forms.FileField()

class SummaryAdmin(admin.ModelAdmin):
    list_display = ('School_ID', 'Sydney_Participant', 'Sydney_Percentile', 'Assessment_Area_Id', 'Award_Id', 'Class_Id')
    
    def get_urls(self):
        urls = super().get_urls()
        new_urls = [path('upload-csv/', self.upload_csv),]
        return new_urls + urls

    def upload_csv(self, request):
        if request.method == "POST":
            csv_file = request.FILES["csv_upload"]
            file_data = csv_file.read().decode("utf-8")
            csv_data = file_data.split("\n")

            for x in csv_data:
                fields = x.split(",")
                created = Summary.objects.update_or_create(
                    School_ID=fields[0],
                    Sydney_Participant=fields[1],
                    Sydney_Percentile=fields[2],
                    Assessment_Area_Id=fields[3],
                    Award_Id=fields[4],
                    Class_Id=fields[5],
                    Corret_answer_percentage_per_class=fields[6],
                    Correct_Answer=fields[7],
                    Student_Id=fields[8],
                    Participant=fields[9],
                    Student_score=fields[10],
                    Subject_Id=fields[11],
                    Category_Id=fields[12],
                    Year_level_name=fields[13],
                    Answer_Id=fields[14],
                    Correct_answer_Id=fields[15],
                    # Add other fields as needed
                )

        form = CsvImportForm()
        data = {"form": form}
        return render(request, "admin/csv_upload.html", data)

admin.site.register(School)
admin.site.register(Class)
admin.site.register(AssessmentArea)
admin.site.register(Student)
admin.site.register(Answers)
admin.site.register(Summary, SummaryAdmin)
admin.site.register(Awards)
admin.site.register(Subject)
