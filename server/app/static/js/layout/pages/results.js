layout.pages.results = (function() {

	var self = {}; 	

	self.bodyCtx = [
[
    ["br"],
    ["br"],
    ["br"],
    ["br"],
        ["div", {"class": "container-fluid", "id": "body-root"},
            ["div", {"class": "pt-2"},
                ["div", {"class": "col-12"},
                    ["div", {"class": "card"},
                        ["div", {"class": "card-header"}, ["b", "Results"]],
                        ["div", {"class": "card-header py-1 bg-white text-right"}],
                        ["div", {"class": "card-body", "style": "overflow-x:auto;"},
                            ["table", {
                                    "id": "example",
                                    "class": "table table-striped table-bordered nowrap",
                                    "style": "width:100%"
                                },
                                ["thead",
                                    ["tr",
                                        ["th", "#"],
                                        ["th", "Date & Time"],
                                        ["th", "File Name"],
                                        ["th", "Hash"],
                                        ["th", "Model"],
                                    ]
                                ],
                                ["tbody",
                                    ["tr",
                                        ["td", "1"],
                                        ["td", "2020-12-01 11:19:11"],
                                        ["td", "00a0f5fe1ba0102ed789b2aa85c3e316.exe"],
                                        ["td",
                                            ["a", {"href": "http://127.0.0.1:5000/#overview?hash=8b6ef43af451d15f62a605925afcd8969cb8b7b24ebd4ff4c73369e8978a2a9d"},
                                                "8b6ef43af451d15f62a605925afcd8969cb8b7b24ebd4ff4c73369e8978a2a9d"
                                            ]
                                        ],
                                        ["td", "c-25.npz"]
                                    ],
                                    ["tr",
                                        ["td", "2"],
                                        ["td", "2021-12-02 05:10:10"],
                                        ["td", "00fbeabd68a647ef625408848c39946c.exe"],
                                        ["td",
                                            ["a", {"href": "http://127.0.0.1:5000/#overview?hash=184030dc9f90ec07531e99ee7da584580c87fc66af3e2c91a2805507e018162e"},
                                                "184030dc9f90ec07531e99ee7da584580c87fc66af3e2c91a2805507e018162e"
                                            ]
                                        ],
                                        ["td", "c-25.npz"]
                                    ],
                                    ["tr",
                                        ["td", "3"],
                                        ["td", "2021-12-03 01:12:10"],
                                        ["td", "0a3ecc1e8f5281b7e9f60a46d1bf0caf.exe"],
                                        ["td",
                                            ["a", {"href": "http://127.0.0.1:5000/#overview?hash=0cb1d9dd01c4d5d4164fd2c8a643ad9b28b04547e953c010e89239e259749d14"},
                                                "0cb1d9dd01c4d5d4164fd2c8a643ad9b28b04547e953c010e89239e259749d14"
                                            ]
                                        ],
                                        ["td", "c-25.npz"],
                                    ],
                                    ["tr",
                                        ["td", "4"],
                                        ["td", "2021-12-03 04:10:19"],
                                        ["td", "0a106cce7ea6f88bbb3f9830664827fb.exe"],
                                        ["td",
                                            ["a", {"href": "http://127.0.0.1:5000/#overview?hash=e752e4ab6c15592fab9588ec00bf5b32ea9f432f458e5cd3db192ad85e509ba3"},
                                                "e752e4ab6c15592fab9588ec00bf5b32ea9f432f458e5cd3db192ad85e509ba3"
                                            ]
                                        ],
                                        ["td", "c-25.npz"]
                                    ],
                                    ["tr",
                                        ["td", "5"],
                                        ["td", "2021-12-03 04:10:19"],
                                        ["td", "0a29134064c19d23dc603947eb8e44a7.exe"],
                                        ["td",
                                            ["a", {"href": "http://127.0.0.1:5000/#overview?hash=138ad0b7d4f6f64be0b7a6227a794662272858a1a2f5665b6c5f9a4e0f282e85"},
                                                "138ad0b7d4f6f64be0b7a6227a794662272858a1a2f5665b6c5f9a4e0f282e85"
                                            ]
                                        ],
                                        ["td", "c-25.npz"]
                                    ],
                                ]
                            ]
                        ]
                    ]
                ]
            ]
        ]
    ]
];

	var getResultsDataFromServer = function() {
		// TODO 
		// Retrieve all past analysis results from server
	}

	var formatResultsData = function() {
		// TODO 
		// Format the results data into table format
	}

	var loadResultsTable = function() {
		// TODO
		// based on results retrieved from the server, popualte the results datatable
	}

	var addEvents = function() {
		console.log("added page results events")
	}

	self.display = function() {
		$('#'+ids['bodyRoot']).html(HTML(self.bodyCtx))

		$('nav .nav-item').removeClass('active');
		// $('#'+ids['navHomeItem']).addClass('active');

		addEvents();
	}

	return self;

})()

