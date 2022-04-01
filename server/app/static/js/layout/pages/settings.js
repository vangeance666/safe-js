layout.pages.settings = (function() {
	let self = {};


	const areYouSureCtx = ["div", {
	        "class": "modal fade",
	        "id": eleIds['settingsClearConfirmForm'],
	        "tabindex": "-1",
	        "aria-labelledby": eleIds['settingsClearConfirmForm'],
	        "style": "display: none;",
	        "aria-hidden": "true"
	    },
	    ["div", {"class": "modal-dialog modal-dialog-centered", "role": "document"},
	        ["div", {"class": "modal-content"},
	            ["div", {"class": "modal-header"},
	                ["h2", {"class": "h6 modal-title"}, "Delete Confirmation"],
	                ["button", {
	                        "type": "button",
	                        "class": "btn-close",
	                        "data-bs-dismiss": "modal",
	                        "aria-label": "Close"
	                    }
	                ]
	            ],
	            ["div", {"class": "modal-body"},
	                ["p",
	                    "By confirming to delete all your past analysis results, the data will not be recoverable."
	                ]
	            ],
	            ["div", {"class": "modal-footer"},
	                ["button", {'id': eleIds['settingsClearConfirmOk'], "type": "button", "class": "btn btn-danger  btn-secondary"},
	                    "Accept"
	                ],
	                ["button", {
	                        "type": "button",
	                        "class": "btn btn-link text-gray-600 ms-auto",
	                        "data-bs-dismiss": "modal"
	                    },
	                    "Close"
	                ]
	            ]
	        ]
	    ]
	]

	const dataControlCardCtx = ["div", {"class": "card card-body border-0 shadow mb-4 mb-xl-0"},
	    ["h2", {"class": "h5 mb-4"}, "Handle your data"],
	    ["ul", {"class": "list-group list-group-flush"},
	        ["li", {
	                "class": "list-group-item d-flex align-items-center justify-content-between px-0 border-bottom"
	            },
	            ["div",
	                ["h3", {"class": "h6 mb-1"}, "Clear all past analysed results"],
	                ["p", {"class": "small pe-4"},
	                    "Delete all past analysed pages results to free space and improve performance."
	                ]
	            ],
	            ["div",
	                ["button", {
	                	'id': eleIds['settingsClearResultsBtn'], 
	                	"class": "btn btn-outline-danger mb-3",
	                	"type": "button",
				        "data-bs-toggle": "modal",
				        "data-bs-target": `#${eleIds['settingsClearConfirmForm']}`}, 
	                	"Clear past results"]
	            ]
	        ]
	    ]
	]

	const sendDeleteRequest = function() {
		console.log("send delete data request");

		$.ajax({

		})
		.done(function(e){

		})
		.fail(function(e) {

		});
	}

	const initEvents = function() {
		layout.banner.setBannerPath(["Page", "Settings"])
		layout.banner.setBannerHeader("Settings")
		layout.banner.setBannerDescription("Change configurations")
		layout.banner.setActionRightButton("")

		
		$('#'+eleIds['settingsClearConfirmOk']).click(function() {
			sendDeleteRequest();
			$('#'+eleIds['settingsClearConfirmForm']).modal('toggle');
		})
	}

	self.ctx = [dataControlCardCtx, areYouSureCtx]

	self.display = function() {
		console.log("Settings display toggled")

		$('#'+eleIds['rootBody']).html(HTML(self.ctx))

		initEvents();
	}

	return self;
})()
