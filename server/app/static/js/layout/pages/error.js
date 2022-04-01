layout.pages.error = (function() {

	let self = {};

	var error404Ctx = ["section", {"class": "vh-100 d-flex align-items-center justify-content-center"},
	    ["div", {"class": "container"},
	        ["div", {"class": "row"},
	            ["div", {
	                    "class": "col-12 text-center d-flex align-items-center justify-content-center"
	                },
	                ["div",
	                    ["img", {
	                            "class": "img-fluid w-75",
	                            "src": "/static/img/illustrations/404.svg",
	                            "alt": "404 not found"
	                        }
	                    ],
	                    ["h1", {"class": "mt-5"},
	                        "Page not",
	                        ["span", {"class": "fw-bolder text-primary"}, "found"]
	                    ],
	                    ["p", {"class": "lead my-4"},
	                        "Oops! Looks like you followed a bad link. If you think this is a problem with us, please tell us."
	                    ]
	                ]
	            ]
	        ]
	    ]
	]

	self.ctx = error404Ctx;

	self.display = function() {
		$('body').html(HTML(self.ctx))
	}


	return self;
})();