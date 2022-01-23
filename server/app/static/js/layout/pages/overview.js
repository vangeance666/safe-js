layout.pages.overview = (function() {

	var self = {}; 	

	var genCardsCtx = function(title, iconCls, bgCls, value) {
		return ['div', {'class': "col 3"}, 
			["div", {"class": "info-box "+bgCls},
			    ["span", {"class": "info-box-icon "+bgCls}, ["i", {"class": iconCls}]],
			    ["div", {"class": "info-box-content"},
			        ["span", {"class": "info-box-text"}, title],
			        ["span", {"class": "info-box-number"}, value],
			        ["div", {"class": "progress"},
			            ["div", {"class": "progress-bar", "style": "width: 100%"}]
			        ]
			    ]
			]
		]
	}



	self.bodyCtx = [
	    ["br"],
	    ["br"],
	    ["br"],
	    ["br"],
    	['div', {'class': 'card card-default'},
          	['div', {'class': 'card-body'},
          		['h1', "Inference Output"],
          		['div', {'class': 'card card-default'},
			      	['div', {'class': 'card-header'}, "Output"],
		          	['div', {'class': 'card-body'},
						['div', {'class': 'row'},
							genCardsCtx('Spyware',"fas fa-user-secret", "bg-info",  "0.00035532397507998404"),
							genCardsCtx('Downloader',"fas fa-download", "bg-info",  "0.0001174639870811583"),
							genCardsCtx('Trojan',"fas fa-horse", "bg-info",  "0.09249786512268318"),
							genCardsCtx('Worm',"fas fa-bug", "bg-info",  "0.0011131791430414267"),
							genCardsCtx('Adware',"fab fa-adversal", "bg-info",  "0.00040034320967589264"),
							genCardsCtx('Virus',"fas fa-viruses", "bg-info",  "0.0005096122506046084"),
							genCardsCtx('Backdoor',"fas fa-door-open", "bg-info",  "0.00157239820265964"),
							genCardsCtx('Ransom',"fas fa-hand-holding-usd", "bg-info",  "0.007544205125407783"),
							genCardsCtx('Miner',"fas fa-hammer", "bg-info",  "0.0006670524844509775"),
							genCardsCtx('Unknown',"fas fa-question-circle", "bg-info",  "0.8952225564993154"),
							genCardsCtx('Malign',"fas fa-skull", "bg-info",  "0.6957522420529288")
						]
		          	]
			    ]
          	]
        ]
	];




	var addEvents = function() {
		
		console.log("added page overview events")
	}

	self.display = function() {
		$('#'+ids['bodyRoot']).html(HTML(self.bodyCtx))

		$('nav .nav-item').removeClass('active');
		// $('#'+ids['navHomeItem']).addClass('active');

		addEvents();
	}

	return self;

})()

