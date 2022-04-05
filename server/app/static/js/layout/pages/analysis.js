layout.pages.analysis = (function() {
	let self = {};


	const ajaxApiAnalyzeUrl = "api/v1_0/analysis/run/"

	const ajaxApiDetailsUrl = "api/v1_0/analysis/details/"

	const submitUrlBtnPath = ["path", {
	        "d": "M14 18h4v-8h6l-8-8-8 8h6zM20 13.5v3.085l9.158 3.415-13.158 4.907-13.158-4.907 9.158-3.415v-3.085l-12 4.5v8l16 6 16-6v-8z"
	    }
	]

	const predictSvgPath = ["path", {
	        "d": "M16 2c8.837 0 16 7.163 16 16 0 6.025-3.331 11.271-8.25 14h-15.499c-4.92-2.729-8.25-7.975-8.25-14 0-8.837 7.163-16 16-16zM25.060 27.060c2.42-2.42 3.753-5.637 3.753-9.060h-2.813v-2h2.657c-0.219-1.406-0.668-2.755-1.33-4h-3.327v-2h2.009c-0.295-0.368-0.611-0.722-0.949-1.060-1.444-1.444-3.173-2.501-5.060-3.119v2.178h-2v-2.658c-0.656-0.102-1.324-0.155-2-0.155s-1.344 0.053-2 0.155v2.658h-2v-2.178c-1.887 0.617-3.615 1.674-5.060 3.119-0.338 0.338-0.654 0.692-0.949 1.060h2.009v2h-3.327c-0.662 1.245-1.111 2.594-1.33 4h2.657v2h-2.813c0 3.422 1.333 6.64 3.753 9.060 0.335 0.335 0.685 0.648 1.049 0.94h6.011l1.143-16h1.714l1.143 16h6.011c0.364-0.292 0.714-0.606 1.049-0.94z"
	    }
	]

	const sendUrlSvgPath = ["path", {
	        "d": "M30.148 5.588c-2.934-3.42-7.288-5.588-12.148-5.588-8.837 0-16 7.163-16 16s7.163 16 16 16c4.86 0 9.213-2.167 12.148-5.588l-10.148-10.412 10.148-10.412zM22 3.769c1.232 0 2.231 0.999 2.231 2.231s-0.999 2.231-2.231 2.231-2.231-0.999-2.231-2.231c0-1.232 0.999-2.231 2.231-2.231z"
	    }
	];

	const analyseUrlConfirmFormCtx = ["div", {
	        "class": "modal fade",
	        "id": eleIds['analysisSubmitUrlForm'],
	        "tabindex": "-1",
	        "aria-labelledby": eleIds['analysisSubmitUrlForm'],
	        "style": "display: none;",
	        "aria-hidden": "true"
	    },
	    ["div", {
	            "class": "modal-dialog modal-tertiary modal-dialog-centered modal-lg",
	            "role": "document"
	        },
	        ["div", {"class": "modal-content bg-dark text-white"},
	            ["div", {"class": "modal-body text-center"},
	                ["span", {"class": "modal-icon"},
	                    ["svg", {
	                            "class": "icon icon-xl text-gray-200",
	                            "fill": "currentColor",
	                            "viewbox": "0 0 32 32",
	                        }, sendUrlSvgPath
	                    ] 
	                ],
	                ["p", {"class": "lead"},
	                    "Enter URL to add to anaylsis queue"
	                ],
	                ["div", {"class": "form-group px-lg-5"},
	                    ["div", {"class": "d-flex mb-3 justify-content-center"},
	                        ["input", {
	                                "type": "text",
	                                "id": eleIds['analysisSubmitUrlFormText'],
	                                "class": "me-sm-1 mb-sm-0 form-control form-control-lg",
	                                "placeholder": "http://xsite.singaporetech.edu.sg"
	                            }
	                        ],
	                        ["div",
	                            ["button", {
	                            		"id": eleIds['analysisSubmitUrlFormOk'],
	                                    "type": "submit",
	                                    "class": "ms-2 btn large-form-btn btn-secondary"
	                                },
	                                "Analyse"
	                            ]
	                        ]
	                    ]
	                ]
	            ]
	        ]
	    ]
	]

	formatRowDataCtx = function(rowData) {
		let res = ['tr'];
		for (let i=0; i < rowData.length-1; i++) {
			res.push(layout.helper.genNormalTd(rowData[i]))
		}
		res.push(layout.helper.genPredictionTd(rowData[rowData.length-1]))
		return res;
	}

	const postUrlForAnalysis = function(urlText) {
		console.log("urlText: ", urlText);

		$.ajax({
			url: ajaxApiAnalyzeUrl,
			contentType: 'application/json',
			type: 'POST',
			data: JSON.stringify({url: urlText}),
			dataType: "json"			
		})
		.done(function(e) {
			console.log("postUrlForAnalysis e: ", e);

			if (!e.status){
				showError("Server not replying status value")
				return
			}
			if (e.status === "error") {
				showError("Server error: "+e.error_message)
				return
			}
			if (!e.page_id) {
				showError("No Page ID returned")
				return
			}
			showSuccess(`Successfully added ${e.url} for analysis`)

		})
		.fail(function(e) {
			showError("Unale to POST url for analysis")
		})
	}

	defaultSetTableData = function(tableBodyId, dataRows) {
		$('#'+tableBodyId).html(HTML(
			[dataRows, function(row) {
					return ['tr',
						row, function(colVal) {
							return layout.helper.genNormalTd(colVal)
						}
					]
				}
			]			
	    ));
	}
	

	setPredictCardValues = function(headerDescription, headerValue) {
		$('#'+eleIds['analysisPredictCardDesc']).text(headerDescription)
		$('#'+eleIds['analysisPredictCardHeader']).text(headerValue)
	}

	setPredictBarValues = function(barTitle, barSpanValue, barPercentInt) {
		$('#'+eleIds['analysisPredictHeaderTitle']).text(barTitle)
		$('#'+eleIds['analysisPredictHeaderSpan']).text(barSpanValue)

		$('#'+eleIds['analysisPredictBar']).attr("aria-valuenow", barPercentInt)
		// $('#'+eleIds['analysisPredictBar']).attr("aria-valuenow", barPercentInt)
		$('#'+eleIds['analysisPredictBar']).css("width", `${barPercentInt}%`)
	}

	const loadAnalysisResultsTable = function(analysisId) {

		
		let allGetParams = window.location.search.substring(1)
		if (allGetParams === "") {
			
			return
		}

		let paramsDict = new URLSearchParams(allGetParams);
		let pageId = paramsDict.get("pageId");
		let jsFileId = layout.helper.stripTrailingSlash(paramsDict.get("jsFileId"))

		if ((pageId === null) || (jsFileId === null)) {
			showError("Invalid page id and js src value")
			return
		}	

		

		$.ajax({
			url: ajaxApiDetailsUrl,
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

			let staticFeaturesHeaders = e.details.static_features.headers
			let dynamicFeaturesHeaders = e.details.dynamic_features.headers

			if (e.details.model_predicted === true && e.details.malign_percent) {
				setPredictCardValues("Malign scale", e.details.malign_percent)
				setPredictBarValues("Malign Percentage",
				 e.details.malign_percent,
				  e.details.malign_percent * 100)
			} 

			if (staticFeaturesHeaders){
				layout.helper.setTableHeaders(eleIds['analysisStaticFtTblHeader'], staticFeaturesHeaders)	
			} 

			if (dynamicFeaturesHeaders) {
				layout.helper.setTableHeaders(eleIds['analysisDyanmicFtTblHeader'], dynamicFeaturesHeaders)	
			} 
			

			let staticValues = e.details.static_features.data
			let dynamicValues = e.details.dynamic_features.data

			if (staticValues) {
				console.log("staticValues: ", staticValues);
				defaultSetTableData(eleIds['analysisStaticFtTblBody'], staticValues)
				// setStaticFeaturesTableData();
			}

			if (dynamicValues) {
				console.log("dynamicValues: ", dynamicValues);
				defaultSetTableData(eleIds['analysisDyanmicFtTblBody'], dynamicValues)
				// setDynamicFeaturesTableData();
			}


			

			// $('#'+eleIds['analysisStaticFtTblMain']).DataTable([]);
			// $('#'+eleIds['analysisDyanmicFtTblMain']).DataTable([]);

				
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
	                // viewBox, svgPath, cardDescId, cardHeaderId)
	            ["div", {"class": "row align-items-center mb-4"},
	                layout.helper.cardDefaultOverviewCtx("0 0 32 32",
	                 predictSvgPath, 
	                 eleIds['analysisPredictCardDesc'], 
	                 eleIds['analysisPredictCardHeader']),
					// Percent bar
					layout.helper.percentDefaultBarCtx(eleIds['analysisPredictHeaderTitle']
						, eleIds['analysisPredictHeaderSpan']
						, eleIds['analysisPredictBar']
						, "bg-danger")
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
	            		layout.helper.halfPageCardCtx("Static Features", staticFtTableCtx),
	            		layout.helper.halfPageCardCtx("Dynamic Features", dynamicFtTableCtx)
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
	    "", {
	        'data-bs-toggle': 'modal',
	        'data-bs-target': '#' + eleIds['analysisSubmitUrlForm']
	    },
	    submitUrlBtnPath,
	    "0 0 32 32",
	    "Submit New URL")


		$('#'+eleIds['analysisSubmitUrlFormOk']).click(function(e) {
			e.preventDefault();

			let urlText = $('#'+eleIds['analysisSubmitUrlFormText']).val();
			if (!urlText || urlText === "") {
				showError("Please key in a valid URL to anaylyse");
				return
			}
			postUrlForAnalysis(urlText);
			$('#'+eleIds['analysisSubmitUrlForm']).modal('toggle');
		})

	}
// btnId, hrefValue, attrsDict, btnSvgPath, viewBox, btnText)
	self.display = function() {
		

		$('#'+eleIds['rootBody']).html(HTML(self.ctx, analyseUrlConfirmFormCtx))
		initEvents();

		loadAnalysisResultsTable();

		setPredictCardValues("Malign scale", "---")
		setPredictBarValues("Malign Percentage", "---", "---")	
	}

	return self;
})()
