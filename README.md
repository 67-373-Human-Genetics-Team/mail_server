#support
## mailer
####sending a message (JSON post data to /send)
request:

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
	
response: HTTP status
	
	
## support data
#### get list of papers (JSON post data to /papers)
request:

	{"name": "Firstname Lastname1"}
response: 

	[
		{
		  "title": "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
		  "journal": "Some Journal",
		  "pub-date": "mm/dd/yyyy",
		  "authors": [
		  	{"name": "Firstname Lastname1",
		  	 "organization": "division name, organization name, address"
		  	},
		  	{"name": "Firstname Lastname2",
		  	 "organization": "division name, organization name, address"
		  	},
		  	{"name": "Firstname Lastname3",
		  	 "organization": "division name, organization name, address"
		  	},
		  	{"name": "Firstname Lastname4",
		  	 "organization": "division name, organization name, address"
		  	},
		  ],
		  "data-source": "pmc",
		  "id": "123456789"
		},
		{...},
		{...},
		{...}
	]
