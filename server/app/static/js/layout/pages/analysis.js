layout.pages.analysis = (function() {
	let self = {};

	const submitUrlBtnPath = ["path", {
	        "d": "M14 18h4v-8h6l-8-8-8 8h6zM20 13.5v3.085l9.158 3.415-13.158 4.907-13.158-4.907 9.158-3.415v-3.085l-12 4.5v8l16 6 16-6v-8z"
	    }
	]

	const predictSvgPath = ["path", {
	        "d": "M16 2c8.837 0 16 7.163 16 16 0 6.025-3.331 11.271-8.25 14h-15.499c-4.92-2.729-8.25-7.975-8.25-14 0-8.837 7.163-16 16-16zM25.060 27.060c2.42-2.42 3.753-5.637 3.753-9.060h-2.813v-2h2.657c-0.219-1.406-0.668-2.755-1.33-4h-3.327v-2h2.009c-0.295-0.368-0.611-0.722-0.949-1.060-1.444-1.444-3.173-2.501-5.060-3.119v2.178h-2v-2.658c-0.656-0.102-1.324-0.155-2-0.155s-1.344 0.053-2 0.155v2.658h-2v-2.178c-1.887 0.617-3.615 1.674-5.060 3.119-0.338 0.338-0.654 0.692-0.949 1.060h2.009v2h-3.327c-0.662 1.245-1.111 2.594-1.33 4h2.657v2h-2.813c0 3.422 1.333 6.64 3.753 9.060 0.335 0.335 0.685 0.648 1.049 0.94h6.011l1.143-16h1.714l1.143 16h6.011c0.364-0.292 0.714-0.606 1.049-0.94z"
	    }
	]

	formatRowDataCtx = function(rowData) {
		let res = ['tr'];
		for (let i=0; i < rowData.length-1; i++) {
			res.push(layout.helper.genNormalTd(rowData[i]))
		}
		res.push(layout.helper.genPredictionTd(rowData[rowData.length-1]))
		return res;
		
	}

	const setStaticFeaturesTableData = function() {

	}
	const setDynamicFeaturesTableData = function() {

	}

	function loadAnalysisResultsTable(analysisId) {

		console.log("loadanalysisResultsTable");
		let allGetParams = window.location.search.substring(1)
		if (allGetParams === "") {
			showError("No ID and JS Src get params found")
			return
		}

		let paramsDict = new URLSearchParams(allGetParams);
		let pageId = paramsDict.get("pageId");
		let jsFileId = layout.helper.stripTrailingSlash(paramsDict.get("jsFileId"))

		if ((pageId === null) || (jsFileId === null)) {
			showError("Invalid page id and js src value")
			return
		}	

		console.log("newjsSrc: ", jsFileId);	
		$.ajax({
			url: "api/v1_0/analysis/details/",
        	type: 'GET',
        	data: {page_id: pageId
        		, js_file_id: jsFileId
        	}
		})
		.done(function(e){
			if (e.status === "error") {
				showError(e.error_message)
				return
			}

			if (!e.details) {
				showError("Invalid Details received from response")
				return
			}

			let staticFeaturesHeaders = Object.keys(e.details.static_features.all)
			console.log("staticFeaturesHeaders: ", staticFeaturesHeaders);
			let dynamicFeaturesHeaders = Object.keys(e.details.dynamic_features.iocs)
			console.log("dynamicFeaturesHeaders: ", dynamicFeaturesHeaders);


			layout.helper.setTableHeaders(eleIds['analysisStaticFtTblHeader'], staticFeaturesHeaders)
			layout.helper.setTableHeaders(eleIds['analysisDyanmicFtTblHeader'], dynamicFeaturesHeaders)


			// setStaticFeaturesTableData();
			// setDynamicFeaturesTableData();

			// $('#'+eleIds['analysisStaticFtTblMain']).DataTable([]);
			// $('#'+eleIds['analysisDyanmicFtTblMain']).DataTable([]);

			console.log(e)	
		})
		.fail(function(e){
			showError("Failed to query analysis results, API down?")
		});

		// var requestResult = $.getJSON("api/v1_0/analysis/results/"+analysisId+"/", function() {

		// 	if (requestResult.status !== 200) {
		// 		showError("Unable to retrieve analysis results");
		// 		return
		// 	}

		// 	if (requestResult.responseText === undefined) {
		// 		showError("Invalid results response");
		// 		return
		// 	}

		// 	jsonData = JSON.parse(requestResult.responseText)

		// 	if (jsonData.headers.length !== jsonData.rows[0].length) {
		// 		showError("Results header and row data different number of columns")
		// 		return
		// 	}

		//   	$('#'+eleIds["analysisTableHeader"]).html(HTML(
		//   		["tr",
		// 			jsonData.headers, function(colHeader) {
		// 				return ["th", {
		// 						"class": "border-bottom",
		// 						"scope": "col"
		// 					}, colHeader							
		// 				]
		// 			}
					
		// 		]
		//     ));

		//   	$('#'+eleIds["analysisTableBody"]).html(HTML(
		// 		jsonData.rows, function(rowData) {
		// 			return formatRowDataCtx(rowData)
		// 		}
		//     ));

		//     $('#'+eleIds["analysisTableMain"]).DataTable();
		// })
	}


	// var analysisTableCardCtx = ['div', {'class': 'card border-0 shadow'},
	// 	["div", {"class": "card-body"},
	// 		["div", {"class": "table-responsive-xxl overflow-auto"},
	// 			["table", {"id": eleIds["analysisTableMain"],
	// 			 "class": "table table-centered table-nowrap mb-0 rounded"},
	// 				["thead", {"id": eleIds["analysisTableHeader"],"class": "thead-light"}], //headers
	// 				["tbody", {"id": eleIds["analysisTableBody"]}] // all data will be put inside
	// 			]
	// 		]
	// 	]
	// ];

	const staticFtTableCtx = layout.helper.tableTemplateCtx(
		eleIds['analysisStaticFtTblMain'],
		eleIds['analysisStaticFtTblHeader'],
		eleIds['analysisStaticFtTblBody'])

	const dynamicFtTableCtx = layout.helper.tableTemplateCtx(
		eleIds['analysisDyanmicFtTblMain'],
		eleIds['analysisDyanmicFtTblHeader'],
		eleIds['analysisDyanmicFtTblBody'])

	const predictionCardCtx = ["div", {"class": "card border-0 shadow mb-5"},
	        ["div", {
	                "class": "card-header border-bottom d-flex align-items-center justify-content-between"
	            },
	            ["h2", {"class": "fs-5 fw-bold mb-0"}, "Prediction"]
	        ],
	        ["div", {"class": "card-body"},
	        	//
	            ["div", {"class": "row align-items-center mb-4"},
	                layout.helper.cardOverviewCtx("0 0 32 32", predictSvgPath, "Malign Probability", "75"),
					// Percent bar
					layout.helper.percentBarCtx("bg-danger", "0.7514", "75")
	                
	            ]
	            //
	        ]
	    ];

	self.ctx = ["div", {"class": "row"},
	    ["div", {"class": "col-12 mb-4"},
	        ["div", {"class": "card border-0 shadow components-section"},
	            ["div", {"class": "card-body"},
	            	["div", {"class": "row mt-3"},

	            		['div', {'class': "row "},

	            			predictionCardCtx
	            		]	            		
	            	],
	            	["div", {"class": "row"},

	            		['div', {'class': "row col-6"},
	            			["div", {"class": ""},
		                        ["div", {"class": "mb-3"},
		                            ["h2", {"class": "h5 mb-1"}, "Static Features"]
		                        ]
		                    ],
		                    ["div", {"class": ""},
		                        ["div", {"class": "mb-3"},
		                        	staticFtTableCtx
		                        ]
		                    ]
	            		],
	            		['div', {'class': "row col-6"},
	            		 	["div", {"class": ""},
		                        ["div", {"class": "mb-3"},
		                            ["h2", {"class": "h5 mb-1"}, "Dynamic Features"]
		                        ]
		                    ],
	            			["div", {"class": ""},
		                        ["div", {"class": "mb-3"},
		                        	dynamicFtTableCtx
		                        ]
		                    ]
		                   
	            		]
	            	]          	

	                
	            ]
	        ]
	    ]
	]



	

	



	const modalSubmitForm = ["div", {
	        "class": "modal fade",
	        "id": eleIds["analysisModalSubmit"],
	        "tabindex": "-1",
	        "aria-labelledby": eleIds["analysisModalSubmit"],
	        "style": "display: none;",
	        "aria-hidden": "true"
	    },
	    ["div", {
	            "class": "modal-dialog modal-tertiary modal-dialog-centered modal-lg",
	            "role": "document"
	        },
	        ["div", {"class": "modal-content bg-dark text-white"},
	            ["div", {"class": "modal-header"},
	                ["button", {
	                        "type": "button",
	                        "class": "btn-close btn-close-white text-white",
	                        "data-bs-dismiss": "modal",
	                        "aria-label": "Close"
	                    }
	                ]
	            ],
	            ["div", {"class": "modal-body text-center py-3"},
	                ["span", {"class": "modal-icon"},
	                    ["svg", {
	                            "class": "icon icon-xl text-gray-200 mb-4",
	                            "fill": "currentColor",
	                            "viewbox": "0 0 20 20",
	                            "xmlns": "http://www.w3.org/2000/svg"
	                        },
	                        ["path", {
	                                "fill-rule": "evenodd",
	                                "d": "M2.94 6.412A2 2 0 002 8.108V16a2 2 0 002 2h12a2 2 0 002-2V8.108a2 2 0 00-.94-1.696l-6-3.75a2 2 0 00-2.12 0l-6 3.75zm2.615 2.423a1 1 0 10-1.11 1.664l5 3.333a1 1 0 001.11 0l5-3.333a1 1 0 00-1.11-1.664L10 11.798 5.555 8.835z",
	                                "clip-rule": "evenodd"
	                            }
	                        ]
	                    ]
	                ],
	                ["h3", {"class": "modal-title mb-3"},
	                    "Join our 1,360,462 subscribers"
	                ],
	                ["p", {"class": "mb-4 lead"},
	                    "Get exclusive access to freebies, premium products and news."
	                ],
	                ["div", {"class": "form-group px-lg-5"},
	                    ["div", {"class": "d-flex mb-3 justify-content-center"},
	                        ["input", {
	                                "type": "text",
	                                "id": "subscribe",
	                                "class": "me-sm-1 mb-sm-0 form-control form-control-lg",
	                                "placeholder": "example@company.com"
	                            }
	                        ],
	                        ["div",
	                            ["button", {
	                                    "type": "submit",
	                                    "class": "ms-2 btn large-form-btn btn-secondary"
	                                },
	                                "Subscribe"
	                            ]
	                        ]
	                    ]
	                ]
	            ],
	            ["div", {"class": "modal-footer z-2 mx-auto text-center"},
	                ["p", {"class": "text-white font-small"},
	                    "We’ll never share your details with third parties.",
	                    ["br", {"class": "visible-md"}],
	                    "View our",
	                    ["a", {"href": "#"}, "Privacy Policy"],
	                    "for more info."
	                ]
	            ]
	        ]
	    ]
	]
	const initEvents = function() {
		layout.banner.setBannerPath(["Page", "Analysis"])
		layout.banner.setBannerHeader("Analysis")
		layout.banner.setBannerDescription("View analysis results based on submission ID")
		layout.banner.setActionRightButton(eleIds["analysisSubmitBtn"],
		 "", submitUrlBtnPath, "0 0 32 32", "Submit New URL")

	}

	self.display = function() {
		console.log("Analysis display toggled")

		$('#'+eleIds['rootBody']).html(HTML(self.ctx))
		initEvents();
		loadAnalysisResultsTable();
	}

	return self;
})()
