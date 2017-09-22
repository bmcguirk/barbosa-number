from rest_framework import viewsets
from barbosa_number.field_reports.serializers import FieldReportSerializer

class FieldReportViewSet(viewsets.ModelViewSet):
    """
    A probably-not-useful API to see all the field reports.
    I'm trying here.
    """
    