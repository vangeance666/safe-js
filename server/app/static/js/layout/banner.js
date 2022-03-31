layout.banner = (function() {

	let self = {};


	var modeSvgCtx = ["path", {"d": "M9.984 6l6 6-6 6-1.406-1.406 4.594-4.594-4.594-4.594z"}]


	self.setBannerPath = function(dirValues) {
		$('#'+eleIds["bannerPath"]).html(HTML(
			["li", {"class": "breadcrumb-item"},
	            ["a", {"href": "#"},
	                ["svg", {
	                        "class": "icon icon-xxs",
	                        "fill": "none",
	                        "stroke": "currentColor",
	                        "viewbox": "0 0 24 24",
	                        // "xmlns": "http://www.w3.org/2000/svg"
	                    },
	                    modeSvgCtx
	                ]
	            ]
	        ], dirValues, function(itemName) {
	        	return["li", {"class": "breadcrumb-item-values breadcrumb-item active"}, ["a", itemName]]
	        }
		))		
	}

	self.setBannerHeader = function(headerValue) {
		$('#'+eleIds['bannerHeader']).text(headerValue);
	}


	self.setBannerDescription = function(description) {
		$('#'+eleIds['bannerDescription']).text(description);
	}

	self.setActionRightButton = function(btnId, hrefValue, btnSvgPath, viewBox, btnText) {
		if (btnId === "") {
			$('#'+eleIds['bannerActionRightButton']).html(HTML(""));
			return 
		}
		
		$('#'+eleIds['bannerActionRightButton']).html(HTML(
			["a", {"id": btnId, "href": hrefValue, "class": "btn btn-outline-gray-600 d-inline-flex align-items-center"},
			    ["svg", {
			        "class": "icon icon-xs me-1",
			        "fill": "currentColor",
			        "viewbox": viewBox,
			        }, btnSvgPath
			    ], btnText
			]

		));
	}

	self.ctx = ["div", {"class": "py-4"},
		    ["nav", {"aria-label": "breadcrumb", "class": "d-none d-md-inline-block"},
		        ["ol", {"id": eleIds["bannerPath"], "class": "breadcrumb breadcrumb-dark breadcrumb-transparent"},
		        	// Path details
		           
		        ]
		    ],
		    ["div", {"class": "d-flex justify-content-between w-100 flex-wrap"},
		        ["div", {"class": "mb-3 mb-lg-0"},
		            ["h1", {"id": eleIds["bannerHeader"], "class": "h4"}, "bannerHeader"],
		            ["p", {"id": eleIds["bannerDescription"], "class": "mb-0"},
		                "---"
		            ]
		        ],
		        ["div", {'id': eleIds['bannerActionRightButton']}
		        	// Optional Right Button do do some actions
		            
		        ]
		    ]
		]

	
	self.addEvents = function() {

		// self.setBannerPath(["Default"])
		// self.setBannerHeader("Default header")
		// self.setBannerDescription("Default Description")
		
		$(".nav-item").click(function(){
			$('.nav-item').removeClass("active");
			$(this).addClass("active");

		})

	// 	console.log("nav added events");
	}

	return self;
})()