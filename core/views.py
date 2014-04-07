from django.http import HttpResponse
from core import models
from django.shortcuts import get_object_or_404, render_to_response, redirect
from django.template import RequestContext
from django.views.decorators.http import require_http_methods, require_POST
from django.core.mail import EmailMessage
from django.views.decorators.csrf import csrf_exempt
from django.template.loader import get_template, render_to_string
from django.core.mail import EmailMultiAlternatives
import json

def index(request):
  return HttpResponse("hello!")

@require_POST
@csrf_exempt
def send(request):
  fromEmail = 'pitt.human.genetics@gmail.com'

  defaultSubject = 'Hello'
  defaultData = {}
  defaultTo = [fromEmail]

  postData = json.loads(request.body)

  subject = postData.get('subject', defaultSubject)
  data = postData.get('data', defaultData)
  toList = postData.get('to', defaultTo)
  templateName = postData.get('template')+'.html'
  
  text_content = ""
  html_content = render_to_string(templateName, data)
  
  email = EmailMultiAlternatives(subject, text_content, fromEmail, toList)
  email.attach_alternative(html_content, "text/html")
  
  if email.send(fail_silently=False) == 1:
    status = 200 #ok
  else:
    status = 400 #error
  return HttpResponse(status=status)
