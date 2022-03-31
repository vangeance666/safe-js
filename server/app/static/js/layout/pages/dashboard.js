layout.pages.dashboard = (function() {
	let self = {};


	const genCardCtx = function(color, imgSrc, labelName, value) {
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

	const rowOneCtx = ["div", {"class": "row"},
		genCardCtx("icon-shape-success", "./static/img/task.svg", "Number of Tasks", "0"),
		genCardCtx("icon-shape-secondary", "./static/img/js_file.svg", "Analysed Files", "2"),
		genCardCtx("icon-shape-danger", "./static/img/danger.svg", "Flagged Files", "1")
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

	const addEvents = function() {
		layout.banner.setBannerPath(["Page", "Dashboard"])
		layout.banner.setBannerHeader("Dashboard")
		layout.banner.setBannerDescription("Overview of all details")
        layout.banner.setActionRightButton("")


	}

	self.display = function() {
		console.log("Dashboard display toggled")
		$('#'+eleIds['rootBody']).html(HTML(self.ctx))

		addEvents();
	}

	return self;

})()
