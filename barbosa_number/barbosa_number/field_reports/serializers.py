from barbosa_number.field_reports import models
from rest_framework import serializers

class FieldReportSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FieldReport
        # fields = ('url', 'username', 'email', 'groups')
        fields = (  'toState',
                    'smsMessageSid',
                    'numMedia',
                    'toCity',
                    'fromZip',
                    'smsSid',
                    'fromState',
                    'smsStatus',
                    'fromCity',
                    'body',
                    'fromCountry',
                    'to',
                    'messagingServiceSid',
                    'toZip',
                    'numSegments',
                    'messageSid',
                    'accountSid',
                    'from',
                    'apiVersion'
                    )