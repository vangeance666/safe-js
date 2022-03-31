layout.helper = (function() {
	let self = {};

	self.genNormalTd = function(data) { 
		return ['td', {'class': "fw-bolder text-gray-500"}, data]
	}

	self.genPredictionTd = function(percentVal) {
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

	self.formatRowDataCtx = function(rowData) {
		let res = ['tr'];
		for (let i=0; i < rowData.length-1; i++) {
			res.push(self.genNormalTd(rowData[i]))
		}
		res.push(self.genPredictionTd(rowData[rowData.length-1]))
		return res;
		
	}

	return self;	
})()