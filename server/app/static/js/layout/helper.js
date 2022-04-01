layout.helper = (function() {
	let self = {};


	self.getParameterByName = function(name, url=window.location.href) {
	    name = name.replace(/[\[\]]/g, '\\$&');
	    var regex = new RegExp('[?&]' + name + '(=([^&#]*)|&|#|$)'),
	        results = regex.exec(url);
	    if (!results) return null;
	    if (!results[2]) return '';
	    return decodeURIComponent(results[2].replace(/\+/g, ' '));
	}

	self.genNormalTdWithProp = function(properties, data) {
		return ['td', properties, data]
	}
	self.genNormalTd = function(data) { 
		return ['td', {'class': "fw-bolder text-gray-500"}, data]
	}

	self.genLinkTd = function(srcLink, data) {
		console.log("srcLink, data: ", srcLink, data);
		return ['a', {'href': srcLink }, data]
		// return ['td', {'class': "fw-bolder text-gray-500"}, 
		// 	['a', {'href': srcLink }, data]
		// ]
	}

	self.genCollapseRow = function(toggle) {


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

	self.setTableHeaders = function(tableHeaderId, headerNames) {
		$('#'+tableHeaderId).html(HTML(
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

	self.tableTemplateCtx = function(tableId, theadId, tbodyId) {
		return ['div', {'class': 'card border-0 shadow'},
			["div", {"class": "card-body"},
				["div", {"class": "table-responsive-xxl overflow-auto"},
					["table", {"id": tableId,
					 "class": "table table-centered table-nowrap mb-0 rounded"},
						["thead", {"id": theadId,"class": "thead-light"}], //headers
						["tbody", {"id": tbodyId}] // all data will be put inside
					]
				]
			]
		];
	}

	self.cardOverviewCtx = function(viewBox, svgPath, cardDesc, cardValue) {
		return ["div", {"class": "col-auto d-flex align-items-center me-5"},
		    ["div", {"class": "icon-shape icon-sm icon-shape-danger rounded me-3"},
		        ["svg", {
		                "fill": "currentColor",
		                "viewbox": viewBox,
		            },svgPath
		            // ["path", {
		            //         "fill-rule": "evenodd",
		            //         "d": "M3 3a1 1 0 000 2v8a2 2 0 002 2h2.586l-1.293 1.293a1 1 0 101.414 1.414L10 15.414l2.293 2.293a1 1 0 001.414-1.414L12.414 15H15a2 2 0 002-2V5a1 1 0 100-2H3zm11 4a1 1 0 10-2 0v4a1 1 0 102 0V7zm-3 1a1 1 0 10-2 0v3a1 1 0 102 0V8zM8 9a1 1 0 00-2 0v2a1 1 0 102 0V9z",
		            //         "clip-rule": "evenodd"
		            //     }
		            // ]
		        ]
		    ],
		    ["div", {"class": "d-block"},
		        ["label", {"class": "mb-0"}, cardDesc],
		        ["h4", {"class": "mb-0"}, cardValue]
		    ]
		]
	}

	self.percentBarCtx = function (colorCls, headerValue, malignPercentValue) {
		return ["div", {"class": "col"},
            ["div", {"class": "progress-wrapper"},
                ["div", {"class": `progress-info`},
                    ["div", {"class": "h6 mb-0"},
                        headerValue
                    ],
                    ["div", {"class": "small fw-bold text-gray-500"},
                        ["span", `${malignPercentValue} %`]
                    ]
                ],
                ["div", {"class": "progress mb-0"},
                    ["div", {
                            "class": `progress-bar ${colorCls}`,
                            "role": "progressbar",
                            "aria-valuenow": `${malignPercentValue}`,
                            "aria-valuemin": "0",
                            "aria-valuemax": "100",
                            "style": `width: ${malignPercentValue}%;`
                        }
                    ]
                ]
            ]
        ]
	}

	self.stripTrailingSlash = function(str) {
    if(str.substr(-1) === '/') {
        return str.substr(0, str.length - 1);
    }
    return str;
}
	self.href = function(hrefValue) {
		window.history.pushState({}, document.title, "/" + hrefValue);
		HTML.route.go();
	}
	
	return self;	
})()