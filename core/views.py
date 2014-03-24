from django.http import HttpResponse
from core import models
from django.shortcuts import get_object_or_404, render_to_response, redirect
from django.template import RequestContext
from django.views.decorators.http import require_http_methods

AUTH_TOKEN = "key-3ax6xnjp29jd6fds4gc373sgvjxteol0"
FROM = "Pitt Human Genetics <publichealth@pitt.edu>"

@require_POST()
def sendMessage(request):
  template = request.POST.template
  address = request.POST.address
  subject = request.POST.subject
  content = request.POST.content # stuff to fill render template with
  status = doSend().status_code
  return HttpResponse(status=status)


def doSend(to, subject, templateName, content):
    template = get_template(templateName)
    message = template.render(content)
    return requests.post(
        "https://api.mailgun.net/v2/messages",
        auth=("api", AUTH_TOKEN),
        data={"from": FROM,
              "to": to,
              "subject": subject,
              "html": message})
