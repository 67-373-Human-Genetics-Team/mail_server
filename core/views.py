# Create your views here.
from django.http import HttpResponse
from core import models
from django.shortcuts import get_object_or_404, render_to_response, redirect
from django.template import RequestContext
from django.views.decorators.http import require_http_methods

AUTH_TOKEN = "key-3ax6xnjp29jd6fds4gc373sgvjxteol0"
FROM = "publichealth@pitt.edu"

#################
##### VIEWS #####
#################

# def index(request):
#     data = {'projectName': 'mailer',
#             'successMessage': "Great success!"}
#     return render_to_response("index.html", data, context_instance=RequestContext(request))

@require_POST()
def sendMessage(request):
  template = request.POST.template
  address = request.POST.address
  subject = request.POST.subject
  content = request.POST.content # stuff to fill render template with

###################
##### HELPERS #####
###################

def send_complex_message():
    return requests.post(
        "https://api.mailgun.net/v2/samples.mailgun.org/messages",
        auth=("api", AUTH_TOKEN),
        data={"from": "Excited User <me@samples.mailgun.org>",
              "to": "foo@example.com",
              "cc": "baz@example.com",
              "bcc": "bar@example.com",
              "subject": "Hello",
              "text": "Testing some Mailgun awesomness!",
              "html": "<html>HTML version of the body</html>"})
