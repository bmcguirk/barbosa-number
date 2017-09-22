from django.db import models
from twilio.twiml.messaging_response import MessagingResponse
from datetime import datetime

class FieldReport(models.Model):
    """
    Class for documenting inbound Twilio text messages. 
    Field documentation here: 
    https://www.twilio.com/docs/api/twiml/sms/twilio_request
    """
    # toState = 
    smsMessageSid = models.CharField(maxlength=34
                                    ,unique=True)
    # numMedia = models.IntegerField()
    # toCity = 
    # fromZip = 
    # fromState = 
    # smsStatus = 
    # fromCity = 
    message_body = models.CharField(maxlength=7)
    men = models.IntegerField()
    women = models.IntegerField()
    hot_dog_stands = models.IntegerField()
    # fromCountry = 
    # to = 
    # messagingServiceSid = 
    # toZip = 
    # numSegments = 
    # messageSid = 
    # accountSid = 
    from_number = models.CharField(maxlength=40)
    # apiVersion = 