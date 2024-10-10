from django.shortcuts import render
from rest_framework import viewsets

from report.entity.report import ResultReport


# Create your views here.
class ResultReportView(viewsets.ViewSet):
    queryset = ResultReport.objects.all()
