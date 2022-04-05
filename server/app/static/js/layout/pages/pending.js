layout.pages.pending = (function() {
	let self = {};


	const pendingTableHeaders = ["ID","Page URL","Status","Error Reason","Crawled","Parsed","Elements Extracted","Analyzed","Features Extracted", "Predicted", "JS Files"]

	const attachJsFileHrefEvent = function() {
		$('.js-file-link').click(function(e){
			e.preventDefault();
			let hrefValue = $(this).attr('href')
			console.log("hrefValue: ", hrefValue);
			layout.helper.href(hrefValue);
			
		});
	}

	const formatRowDataCtx = function(rowDict) {
		let collapseProperty = {
				"class": "btn-sm clickable",
		        "data-bs-toggle": "collapse",
		        "data-bs-target": `#results-hidden-row-${rowDict['id']}`,
		        "href": `#results-hidden-row-${rowDict['id']}`,
		        "aria-expanded": "false",
		        "aria-controls": `#results-hidden-row-${rowDict['id']}`
	        }

		let mainRow =  ['tr', 

			layout.helper.genNormalTd(rowDict['id']),
			layout.helper.genNormalTd(rowDict['page_url']),
			layout.helper.genNormalTd(rowDict['status']),
			layout.helper.genNormalTd(rowDict['error_reason']),
			layout.helper.genNormalTd(rowDict['crawl_success'] ? "✔" : "❌"),
			layout.helper.genNormalTd(rowDict['elements_parsed'] ? "✔" : "❌"),
			layout.helper.genNormalTd(rowDict['js_elements_extracted'] ? "✔" : "❌"),
			layout.helper.genNormalTd(rowDict['is_analyzed'] ? "✔" : "❌"),
			layout.helper.genNormalTd(rowDict['features_extracted'] ? "✔" : "❌"),
			layout.helper.genNormalTd(rowDict['predicted'] ? "✔" : "❌"),

			// layout.helper.genNormalTd(rowDict['id']),
			// layout.helper.genNormalTd(rowDict['page_url']),
			// layout.helper.genNormalTd(rowDict['static_done']),
			// layout.helper.genNormalTd(rowDict['dynamic_done']),
			layout.helper.genNormalTdWithProp(collapseProperty, rowDict['js_file_details'] ? "➕" : "")			
			// layout.helper.genNormalTd(rowDict['js_file_details'] ? "+" : "")			
		]

		let colSpan = Object.keys(rowDict).length

		let collapseRow = ['tr', {'class': 'hide-table-padding accordion-body collapse', 'id': `results-hidden-row-${rowDict['id']}`},
			['td', {"colspan": "12"},
				['div', {'class': 'mx-5'},
					['h5', "JS Files"]
				],

				rowDict['js_file_details'], function(jsFileDict) {

					if (!jsFileDict['static_features_done'] || !jsFileDict['dynamic_features_done'])
						return ['div', {'class': 'mx-5'},
	        				['a', {'class':'js-file-link text-danger'},
	        					jsFileDict['src']]
	        			]	
					else {
						return ['div', {'class': 'mx-5'},
	        				['a', {'class':'js-file-link text-success',
	        					'href':`?pageId=${rowDict['id']}&jsFileId=${jsFileDict['id']}/#/analysis`},
	        					jsFileDict['src']]
	        			]	
					}
        			
        		}				
			]
		]

	    return [mainRow, collapseRow]
	}
	
	const setTableHeaders = function(headerNames) {
		$('#'+eleIds["pendingTableHeader"]).html(HTML(
	  		["tr",
				headerNames, function(colHeader) {
					return ["th", {
							"class": "border-bottom",
							"scope": "col"
						},
						colHeader
					]
				}
				
			]
	    ));
	}

	const setTableData = function(headersRows) {
		$('#'+eleIds["pendingTableBody"]).html(HTML(
			headersRows, function(rowDict) {
				console.log("rowDict: ", rowDict);
				return formatRowDataCtx(rowDict)
			}
	    ));
	}

	function loadTableData() {

		console.log("loadTableData");

		var requestResult = $.getJSON("api/v1_0/analysis/pending/", function() {
			console.log( "success" );
			console.log("requestResult: ", requestResult);

			if (requestResult.status !== 200) {
				showError("Unable to retrieve pending results");
				return
			}

			if (requestResult.responseText === undefined) {
				showError("Invalid results response");
				return
			}

			jsonData = JSON.parse(requestResult.responseText)

			if (jsonData.status === "error") {
				showError("Server error: "+jsonData.error_message)
				return
			}		
			console.log("jsonData.details: ", jsonData.details);
			$('#'+eleIds["pendingTableMain"]).DataTable();
			setTableData(jsonData.details);					  	
			
			attachJsFileHrefEvent();
		    
		})
	}

	var pendingTableCardCtx = layout.helper.tableTemplateCtx(
			eleIds["pendingTableMain"], 
			eleIds["pendingTableHeader"],
			eleIds["pendingTableBody"]
		)

	self.ctx = [pendingTableCardCtx];

	var initEvents = function() {
		layout.banner.setBannerPath(["Page", "pending"])
		layout.banner.setBannerHeader("Pending Analysis")
		layout.banner.setBannerDescription("Summary of submissions which are pending")
		layout.banner.setActionRightButton("")

	}

	self.display = function() {
		console.log("pending display toggled")
		$('#'+eleIds['rootBody']).html(HTML(self.ctx))
		initEvents();

		setTableHeaders(pendingTableHeaders);
		loadTableData();
	}

	return self;
})()
