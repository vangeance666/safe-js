layout.nav = (function() {
	
	var self = {};


	self.ctx = ["nav", {
	        "class": "navbar navbar-expand-lg navbar-expand-lg navbar-light bg-light fixed-top py-0"
	    },
	    ["div", {"class": "collapse navbar-collapse"},
	        ["a", {
	                "class": "nav-link",
	                "style": "padding-right:30px;padding-left:30px;",
	                "href": "/"
	            },
	            ["img", {"src": "/static/img/logo.png"}]
	        ],
	        ["ul", {"class": "navbar-nav mr-auto"},
	            ["li", {"class": "nav-item navBtn"},
	                ["a", {
	                        "class": "nav-link",
	                        "href": NAV_URLS['upload']
	                    },
	                    ["span", {"class": "fas fa-upload"}],
	                    "  Upload"
	                ]
	            ],
	            ["li", {"class": "nav-item navBtn"},
	                ["a", {
	                        "class": "nav-link",
	                        "href": NAV_URLS['overview']
	                    },
	                    ["span", {"class": "fas fa-clipboard-list"}],
	                    "  Overview"
	                ]
	            ],
	            ["li", {"class": "nav-item navBtn"},
	                ["a", {
	                        "class": "nav-link",
	                        "href": NAV_URLS['results']
	                    },
	                    ["span", {"class": "fas fa-poll-h"}],
	                    "  Results"
	                ]
	            ],
	            ["li", {"class": "nav-item navBtn"},
	                ["a", {
	                        "class": "nav-link",
	                        "href": NAV_URLS['modelStatistics']
	                    },
	                    ["span", {"class": "fas fa-chart-pie"}],
	                    "  Model Statistics"
	                ]
	            ]
	        ]
	    ]
	];

	self.addEvents = function() {
		// 1 Each button to toggle different view
		// 2 Ensure that clicking each button will also highlight the button
		$('.'+eleClass['navBtn']).click(function(){
			$('.'+eleClass['navBtn']).removeClass("active");
			$(this).addClass("active");
			console.log("Clicked on nav item");
		});
		console.log("nav added events");
	}

	return self;

})();