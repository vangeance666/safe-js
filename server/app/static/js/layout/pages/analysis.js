layout.pages.analysis = (function() {
	let self = {};

	const submitUrlBtnPath = ["path", {
	        "d": "M14 18h4v-8h6l-8-8-8 8h6zM20 13.5v3.085l9.158 3.415-13.158 4.907-13.158-4.907 9.158-3.415v-3.085l-12 4.5v8l16 6 16-6v-8z"
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

	function loadAnalysisResultsTable(analysisId) {

		console.log("loadanalysisResultsTable");

		let allGetParams = window.location.search.substring(1)

		if (allGetParams === "") {
			showError("No ID and JS Src get params found")
			return
		}

		let paramsDict = new URLSearchParams(allGetParams);
		console.log("paramsDict: ", paramsDict);

		let pageId = paramsDict.get("pageId");
		console.log("pageId: ", pageId);

		let jsFileId = layout.helper.stripTrailingSlash(paramsDict.get("jsFileId"))
		console.log("jsFileId: ", jsFileId);


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


			console.log(e)	
		})

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


	var analysisTableCardCtx = ['div', {'class': 'card border-0 shadow'},
		["div", {"class": "card-body"},
			["div", {"class": "table-responsive-xxl overflow-auto"},
				["table", {"id": eleIds["analysisTableMain"],
				 "class": "table table-centered table-nowrap mb-0 rounded"},
					["thead", {"id": eleIds["analysisTableHeader"],"class": "thead-light"}], //headers
					["tbody", {"id": eleIds["analysisTableBody"]}] // all data will be put inside
				]
			]
		]
	];

	self.ctx = [analysisTableCardCtx];

	const initEvents = function() {
		layout.banner.setBannerPath(["Page", "Analysis"])
		layout.banner.setBannerHeader("Analysis")
		layout.banner.setBannerDescription("View analysis results based on submission ID")
		layout.banner.setActionRightButton(eleIds["analysisSubmitBtn"],
		 "", submitUrlBtnPath, "0 0 32 32", "Submit URL")

	}

	self.display = function() {
		console.log("Analysis display toggled")

		$('#'+eleIds['rootBody']).html(HTML(self.ctx))
		initEvents();
		loadAnalysisResultsTable();
	}

	return self;
})()
