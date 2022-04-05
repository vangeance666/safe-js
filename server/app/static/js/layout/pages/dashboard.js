layout.pages.dashboard = (function() {
	let self = {};


    const genCardCtx = function(eleId, color, imgSrc, labelName, value) {
		return ["div", {"id": eleId, "class": "col-12 col-sm-6 col-xl-4 mb-4"},
            ["div", {"class": "dashboard-card card border-0 shadow"},
                ["div", {"class": "card-body"},
                    ["div", {"class": "row d-block d-xl-flex align-items-center"},
                        ["div", {
                                "class": "col-12 col-xl-5 text-xl-center mb-3 mb-xl-0 d-flex align-items-center justify-content-xl-center"
                            },
                            ["div", {
                                    "class": "icon-shape rounded me-4 me-sm-0 "+ color
                                },
                                ['img', {'src': imgSrc}]
                            ],
                            ["div", {"class": "d-sm-none"},
                                ["h2", {"class": "h5"}, labelName],
                                ["h3", {"class": "results-value fw-extrabold mb-1"}, value]
                            ]
                        ],
                        ["div", {"class": "col-12 col-xl-7 px-xl-0"},
                            ["div", {"class": "d-none d-sm-block"},
                                ["h2", {"class": "h6 text-gray-400 mb-0"},
                                   labelName
                                ],
                                ["h3", {"class": "results-value fw-extrabold mb-2"}, value]
                            ]
                        ]
                    ]
                ]
            ]
        ];
	}

	const rowOneCtx = ["div", {"class": "row"},
		genCardCtx(eleIds['dashboardPagesAnalysed'], "icon-shape-success", "/static/img/pages.svg", "Pages Analysed", "0"),
		genCardCtx(eleIds['dashboardJsFilesAnalysed'], "icon-shape-secondary", "/static/img/js_file.svg", "JS Files Analysed", "2"),
		genCardCtx(eleIds['dashboardFlaggedFiles'], "icon-shape-danger", "/static/img/danger2.svg", "Flagged Files", "1")
    ]

    const rowTwoCtx = 
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

	// self.ctx = 	["main", {"class": "content"},
	// 	rowOneCtx
	// ]

	self.ctx = [rowOneCtx];

    function loadDashboardStats() {

        console.log("loadDashboardStats");

        var requestResult = $.getJSON("api/v1_0/analysis/statistics/", function() {

            if (requestResult.status !== 200) {
                showError("Unable to retrieve recent results");
                return
            }

            if (requestResult.responseText === undefined) {
                showError("Invalid results response");
                return
            }

            jsonData = JSON.parse(requestResult.responseText)

            if (jsonData.status === "error"){
                showError(jsonData.error_message)
                return
            }

            $('#dashboard-pages-analysed')
            $('#'+eleIds['dashboardPagesAnalysed']+" .results-value").text(jsonData.details.pages_analyzed)
            $('#'+eleIds['dashboardJsFilesAnalysed']+" .results-value").text(jsonData.details.js_file_analysed)
            $('#'+eleIds['dashboardFlaggedFiles']+" .results-value").text(jsonData.details.predict_flagged_files)


        })
    }

	const initEvents = function() {
		layout.banner.setBannerPath(["Page", "Dashboard"])
		layout.banner.setBannerHeader("Dashboard")
		layout.banner.setBannerDescription("Overview of all details")
        layout.banner.setActionRightButton("")



	}

	self.display = function() {
		console.log("Dashboard display toggled")
		$('#'+eleIds['rootBody']).html(HTML(self.ctx))

		initEvents();
        loadDashboardStats();
	}

	return self;

})()
