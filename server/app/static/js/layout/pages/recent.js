layout.pages.recent = (function() {
	let self = {};

	function loadRecentResultsTable() {

		console.log("loadRecentResultsTable");

		var requestResult = $.getJSON("api/v1_0/analysis/results/", function() {
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

			if (jsonData.headers.length !== jsonData.rows[0].length) {
				showError("Results header and row data different number of columns")
				return
			}

		  	$('#'+eleIds["recentTableHeader"]).html(HTML(
		  		["tr",
					jsonData.headers, function(colHeader) {
						return ["th", {
								"class": "border-bottom",
								"scope": "col"
							},
							colHeader
						]
					}
					
				]
		    ));

		  	$('#'+eleIds["recentTableBody"]).html(HTML(
				jsonData.rows, function(rowData) {
					return layout.helper.formatRowDataCtx(rowData)
				}
		    ));

		    $('#'+eleIds["recentTableMain"]).DataTable();
		})

	}

	var recentTableCardCtx = ['div', {'class': 'card border-0 shadow'},
		["div", {"class": "card-body"},
			["div", {"class": "table-responsive-xxl overflow-auto"},
				["table", {"id": eleIds["recentTableMain"],
				 "class": "table table-centered table-nowrap mb-0 rounded"},
					["thead", {"id": eleIds["recentTableHeader"],"class": "thead-light"}], //headers
					["tbody", {"id": eleIds["recentTableBody"]}] // all data will be put inside
				]
			]
		]
	];
	

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
		loadRecentResultsTable();
	}

	return self;
})()
