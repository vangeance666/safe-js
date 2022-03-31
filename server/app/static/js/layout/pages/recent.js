layout.pages.recent = (function() {
	let self = {};

	var genNormalTd = function(data) { 
		return ['td', {'class': "fw-bolder text-gray-500"}, data]
	}

	var genPredictionTd = function(percentVal) {
		console.log("percentVal: ", percentVal);
		return ['td', {'class': "fw-bolder text-gray-500"}, 
			["div", {"class": "row d-flex align-items-center"},
				["div", {"class": "col-12 col-xl-2 px-0"},
					["div", {"class": "small fw-bold"}, percentVal+"%"]
				],
				["div", {"class": "col-12 col-xl-10 px-0 px-xl-1"},
					["div", {"class": "progress progress-lg mb-0"},
						["div", {
								"class": "progress-bar bg-dark",
								"role": "progressbar",
								"aria-valuemin": "0",
								"aria-valuemax": "100",
								"style": "width: "+percentVal+"%;",
								"aria-valuenow": percentVal
							}
						]
					]
				]
			]
		];
	}

	formatRowDataCtx = function(rowData) {
		let res = ['tr'];
		for (let i=0; i < rowData.length-1; i++) {
			res.push(genNormalTd(rowData[i]))
		}
		res.push(genPredictionTd(rowData[rowData.length-1]))
		return res;
		
	}

	genRowsDataCtx = function(rows) {
		let ret = [];
		for (let i=0; i < rows.length; i++) {
			ret.push(formatRowDataCtx(rows[i]))
		}
		return ret;
	}



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
					return formatRowDataCtx(rowData)
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

	var addEvents = function() {
		layout.banner.setBannerPath(["Page", "Recent"])
		layout.banner.setBannerHeader("Recent Analysis")
		layout.banner.setBannerDescription("Summary of past submissions")
		layout.banner.setActionRightButton("")

	}

	self.display = function() {
		console.log("Recent display toggled")
		$('#'+eleIds['rootBody']).html(HTML(self.ctx))
		addEvents();
		loadRecentResultsTable();
	}

	return self;
})()
