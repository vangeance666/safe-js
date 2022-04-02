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

	self.genDefaultTr = function(rowData) { 
		return ['tr', 
			rowData, function(x){
				return
			}
		]
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

	


	self.tableTemplateCtx = function(tableId, theadId, tbodyId, tblHeight) {
		return ['div', {'class': 'card border-0 shadow'},
			["div", {"class": "card-body"},
				["div", {"class": "table-responsive-xxl overflow-auto", "style": `height: ${tblHeight ? tblHeight : "600px"}`},
					["table", {"id": tableId,
					 "class": "table table-centered table-nowrap mb-0 rounded"},
						["thead", {"id": theadId,"class": "thead-light"}], //headers
						["tbody", {"id": tbodyId}] // all data will be put inside
					]
				]
			]
		];
	}

	self.cardDefaultOverviewCtx = function(viewBox, svgPath, cardDescId, cardHeaderId) {
		return ["div", {"class": "col-auto d-flex align-items-center me-5"},
		    ["div", {"class": "icon-shape icon-sm icon-shape-danger rounded me-3"},
		        ["svg", {
		                "fill": "currentColor",
		                "viewbox": viewBox,
		            }, svgPath
		        ]
		    ],
		    ["div", {"class": "d-block"},
		        ["label", {'id': cardDescId, "class": "mb-0"}, "Default Description"],
		        ["h4", {'id': cardHeaderId,"class": "mb-0"}, "---"]
		    ]
		]
	}


	self.percentDefaultBarCtx = function (headerId, headerSpanId, barId, colorCls) {
		return ["div", {"class": "col"},
            ["div", {"class": "progress-wrapper"},
                ["div", {"class": `progress-info`},
                    ["div", {'id': headerId, "class": "h6 mb-0"},
                        "Default"
                    ],
                    ["div", {"class": "small fw-bold text-gray-500"},
                        ["span", {'id': headerSpanId},  `0 %`]
                    ]
                ],
                ["div", {"class": "progress mb-0"},
                    ["div", {
                    		'id': barId,
                            "class": `progress-bar ${colorCls}`,
                            "role": "progressbar",
                            "aria-valuenow": `0`,
                            "aria-valuemin": "0",
                            "aria-valuemax": "100",
                            "style": `width: 0%;`
                        }
                    ]
                ]
            ]
        ]
	}


	self.halfPageCardCtx = function(headerText, bodyElement) {
		return ['div', {'class': "row col-6"},
			["div", {"class": ""},
                ["div", {"class": "mb-3"},
                    ["h2", {"class": "h5 mb-1"}, headerText]
                ]
            ],
            ["div", {"class": ""},
                ["div", {"class": "mb-3"},
                	bodyElement
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