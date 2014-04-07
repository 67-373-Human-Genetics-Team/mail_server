#mailer

####example JSON post data (send to /send)

	{
	  "subject": "hi there",
	  "template": "testMessage",
	  "data": {
	    "name": "Firstname Lastname"
	  },
	  "to": [
    	"person@example.com"
  	  ]
	}