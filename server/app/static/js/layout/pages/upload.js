layout.pages.upload = (function() {

	var self = {}; 	


	self.bodyCtx = [
    ["br"],
    ["br"],
    ["br"],
    ["br"],
    ["div", {"class": "container-fluid", "id": "body-root"},
        ["div", {"class": "pt-3"},
            ["div", {"class": "col-12"},
                ["div", ["h3", ["b", "Upload"]], ["br"]],
                ["div", {"class": "card"},
                    ["div", {"class": "card-header"},
                        ["b", "Accepts only DLL, EXE and ZIP file"]
                    ],
                    ["div", {"class": "card-header text-right py-1 bg-white "}],
                    ["div", {"class": "card-body", "style": "overflow-x:auto;"},
                        ["div", {"class": "center"},
                            ["form", {
                                    "action": "",
                                    "method": "POST",
                                    "enctype": "multipart/form-data",
                                    "class": "form-horizontal"
                                },
                                ["div", {"class": "controls"},
                                    ["div", {
                                            "class": "entry input-group upload-input-group"
                                        },
                                        ["input", {
                                                "class": "form-control",
                                                "name": "fields[]",
                                                "type": "file"
                                            }
                                        ],
                                        ["button", {
                                                "class": "btn btn-upload btn-success btn-add",
                                                "type": "button"
                                            },
                                            ["i", {"class": "fa fa-plus"}]
                                        ]
                                    ]
                                ],
                                ["br"],
                                ["button", {"id": ids['pageUploadSelectFileInput'] ,"class": "btn btn-primary"},
                                    ["i", {"class": "fa fa-upload"}],
                                    " Upload"
                                ]
                            ]
                        ]
                    ]
                ]
            ]
        ]
    ]
];



	var uploadMalwareFiles = function() {
		// TODO
		// Upload the malware files to a certain folder at server side
		
	}

	var sendForAnalysis = function () {
		// TODO
		// 1. call uploadfiles
		// 2. Send POST signal through to sieve through those files within the uploaded folder
		// 3. Based on response Toast message. 
		 
	
	}

	var submitFilesToServer = function() {
		$.ajax({
			'async': false,
		    type: "POST",
		    contentType: "application/json", //Tell them sending json
		    url: "api/upload/",
		    dataType: "json", //Receive json
		    data: JSON.stringify({"mode": "upload"})

		}).done(function (e) {	

			var res = e;

			if (res['message'] === "success") {
				showSuccess("Successfully uploaded malwares")
			} else {
				showError("Failed to upload malwares")
			}


			var models = e;
			console.log("e: "+ e);
			console.log("models: ", models);

			$('#'+ids['modelStatsModelSelect']).html(HTML(["select", {"id": ids['modelStatsModelSelect'], "class": "form-select", "aria-label": "Default select example"},
		        ["option", {"selected": "selected"}, "Open this select menu"],
		        models['data'], function(x) {
		        	return ['option', {'value': x}, x]
		        }
		    ]));

		});
	}
	// STOPPED HERE
	var resetFilesInput = function() {
		$('#'+ids['bodyRoot']).html(HTML(self.bodyCtx));
	}


	var addEvents = function() {
		$('#' + ids['pageUploadFileUploadBtn']).click(function(e){
			e.preventDefault();
			
			showSuccess("pageUploadFileUploadBtn");
		});
		$('#' + ids['pageUploadSelectFileInput']).click(function(e){
			e.preventDefault();

			sendForAnalysis();
			showSuccess("Sucessfully uploaded files");
			$('#'+ids['bodyRoot']).html(HTML(self.bodyCtx))



		});

		$("#"+ids['pageUploadSelectFileInput']).click(function(e) {
			e.preventDefault();


		});

		console.log("added page upload events")
	}

	self.display = function() {
		$('#'+ids['bodyRoot']).html(HTML(self.bodyCtx))

		$('nav .nav-item').removeClass('active');
		// $('#'+ids['navHomeItem']).addClass('active');

		addEvents();
	}

	return self;

})()