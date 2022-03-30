layout.pages.dashboard = (function() {
	var self = {};


	var genCardCtx = function(color, imgSrc, labelName, value) {
		return ["div", {"class": "col-12 col-sm-6 col-xl-4 mb-4"},
            ["div", {"class": "card border-0 shadow"},
                ["div", {"class": "card-body"},
                    ["div", {"class": "row d-block d-xl-flex align-items-center"},
                        ["div", {
                                "class": "col-12 col-xl-5 text-xl-center mb-3 mb-xl-0 d-flex align-items-center justify-content-xl-center"
                            },
                            ["div", {
                                    "class": "icon-shape rounded me-4 me-sm-0 "+ color
                                },
                                ["img", {"src": imgSrc}]
                            ],
                            ["div", {"class": "d-sm-none"},
                                ["h2", {"class": "h5"}, labelName],
                                ["h3", {"class": "fw-extrabold mb-1"}, value]
                            ]
                        ],
                        ["div", {"class": "col-12 col-xl-7 px-xl-0"},
                            ["div", {"class": "d-none d-sm-block"},
                                ["h2", {"class": "h6 text-gray-400 mb-0"},
                                   labelName
                                ],
                                ["h3", {"class": "fw-extrabold mb-2"}, value]
                            ]
                        ]
                    ]
                ]
            ]
        ];
	}



	var genTrCtx = function() {
		["tr",
            ["th", {
                    "class": "text-gray-900",
                    "scope": "row"
                },
                "/demo/admin/index.html"
            ],
            ["td", {
                    "class": "fw-bolder text-gray-500"
                },
                "3,225"
            ],
            ["td", {
                    "class": "fw-bolder text-gray-500"
                },
                "$20"
            ],
            ["td", {
                    "class": "fw-bolder text-gray-500"
                },
                ["div", {"class": "d-flex"},
                    ["svg", {
                            "class": "icon icon-xs text-danger me-2",
                            "fill": "currentColor",
                            "viewbox": "0 0 20 20",
                            "xmlns": "http://www.w3.org/2000/svg"
                        },
                        ["path", {
                                "fill-rule": "evenodd",
                                "d": "M5.293 7.707a1 1 0 010-1.414l4-4a1 1 0 011.414 0l4 4a1 1 0 01-1.414 1.414L11 5.414V17a1 1 0 11-2 0V5.414L6.707 7.707a1 1 0 01-1.414 0z",
                                "clip-rule": "evenodd"
                            }
                        ]
                    ],
                    "42,55%"
                ]
            ]
        ]
	}

	var genTableCtx = function(headerColNames, rowDatas) {
		// Cols
		// Page URL, No of internal JS Files, No of external JS files
		return ["div", {"class": "table-responsive"},
            ["table", {
                    "class": "table align-items-center table-flush"
                },
                ["thead", {"class": "thead-light"},
                    ["tr",
                    	headerColNames, function(colName) {
	                    	return ["th", {
	                                "class": "border-bottom",
	                                "scope": "col"
	                            },
	                            colName
	                        ]
	                    }
                        
                    ]
                ],
                ["tbody",
	                rowDatas, function(rowData) {
	                	return ['tr',
	                		rowData, function(data) {
	                			return ['td', {'class': "fw-bolder text-gray-500"}, data]
	                		}
	                	]
	                }
                    // Put TRs here
                ]
            ]
        ];
	}


	var rowOneCtx = ["div", {"class": "row"},
		genCardCtx("icon-shape-success", "./static/img/task.svg", "Number of Tasks", "0"),
		genCardCtx("icon-shape-secondary", "./static/img/js_file.svg", "Analysed Files", "2"),
		genCardCtx("icon-shape-danger", "./static/img/danger.svg", "Flagged Files", "1")
    ]

    var rowTwoCtx = 
    ["div", {"class": "row"},
        ["div", {"class": "col-12 col-xl-12"},
            ["div", {"class": "row"},
                

                ["div", {"class": "col-12 mb-4"},
                    ["div", {"class": "card border-0 shadow"},

                    	// Card headere
                        ["div", {"class": "card-header"},
                            ["div", {"class": "row align-items-center"},
                                ["div", {"class": "col"},
                                    ["h2", {"class": "fs-5 fw-bold mb-0"},
                                        "Page visits"
                                    ]
                                ],
                                ["div", {"class": "col text-end"},
                                    ["a", {
                                            "href": "#",
                                            "class": "btn btn-sm btn-primary"
                                        },
                                        "See all"
                                    ]
                                ]
                            ]
                        ],

                        // Table
                        // End of table
                    ]
                ]
            ]
        ]
    ]

	self.ctx = 	["main", {"class": "content"},
		rowOneCtx
	]

	var addEvents = function() {

	}

	self.display = function() {

		$('#'+ids['rootBody']).html(HTML(self.ctx))

		addEvents();
	}

	return self;

})()
