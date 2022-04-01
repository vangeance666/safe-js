layout.pages.recent = (function() {
	let self = {};


	const recentTableHeaders = ["ID", "Page URL", "Static analysis Status", "Dynamic analysis Status", "JS Files"]

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
			layout.helper.genNormalTd(rowDict['static_done']),
			layout.helper.genNormalTd(rowDict['dynamic_done']),
			layout.helper.genNormalTdWithProp(collapseProperty, rowDict['js_file_details'] ? "+" : "")			
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
		$('#'+eleIds["recentTableHeader"]).html(HTML(
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
		$('#'+eleIds["recentTableBody"]).html(HTML(
			headersRows, function(rowDict) {
				console.log("rowDict: ", rowDict);
				return formatRowDataCtx(rowDict)
			}
	    ));
	}

	function loadTableData() {

		console.log("loadTableData");

		var requestResult = $.getJSON("api/v1_0/analysis/overview/", function() {
			console.log( "success" );
			console.log("requestResult: ", requestResult);

			if (requestResult.status !== 200) {
				showError("Unable to retrieve recent results");
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
			// $('#'+eleIds["recentTableMain"]).DataTable();
			setTableData(jsonData.details);					  	
			
			attachJsFileHrefEvent();

			// $('#'+eleIds["recentTableMain"]).DataTable();
			
		    
		})
	}

	var recentTableCardCtx = layout.helper.tableTemplateCtx(
			eleIds["recentTableMain"], 
			eleIds["recentTableHeader"],
			eleIds["recentTableBody"]
		)

	self.ctx = [recentTableCardCtx];

	var initEvents = function() {
		layout.banner.setBannerPath(["Page", "Recent"])
		layout.banner.setBannerHeader("Recent Analysis")
		layout.banner.setBannerDescription("Summary of past submissions")
		layout.banner.setActionRightButton("")

	}

	self.display = function() {
		console.log("Recent display toggled")
		$('#'+eleIds['rootBody']).html(HTML(self.ctx))
		initEvents();

		setTableHeaders(recentTableHeaders);
		loadTableData();
	}

	return self;
})()
