layout.nav = (function() {
	
	let self = {};

	const dashboardPathCtx = ["path", {
	        "d": "M18 12.984v3h3v2.016h-3v3h-2.016v-3h-3v-2.016h3v-3h2.016zM3 12.984h8.016v8.016h-8.016v-8.016zM12.984 3h8.016v8.016h-8.016v-8.016zM3 3h8.016v8.016h-8.016v-8.016z"
	    }
	]

	const recentPathCtx = ["path", {
	        "d": "M10 14v8h-4v-8h4zM16 6v16h-4v-16h4zM32 24v2h-32v-24h2v22h30zM22 10v12h-4v-12h4zM28 4v18h-4v-18h4z"
	    }
	]

	const analysisPathCtx = ["path", {
	        "d": "M32 10.909l-0.024-0.116-0.023-0.067c-0.013-0.032-0.024-0.067-0.040-0.1-0.004-0.024-0.020-0.045-0.027-0.067l-0.047-0.089-0.040-0.067-0.059-0.080-0.061-0.060-0.080-0.060-0.061-0.040-0.080-0.059-0.059-0.053-0.020-0.027-14.607-9.772c-0.463-0.309-1.061-0.309-1.523 0l-14.805 9.883-0.051 0.053-0.067 0.075-0.049 0.060-0.067 0.080c-0.027 0.023-0.040 0.040-0.040 0.061l-0.067 0.080-0.027 0.080c-0.027 0.013-0.027 0.053-0.040 0.093l-0.013 0.067c-0.025 0.041-0.025 0.081-0.025 0.121v9.996c0 0.059 0.004 0.12 0.013 0.18l0.013 0.061c0.007 0.040 0.013 0.080 0.027 0.115l0.020 0.067c0.013 0.036 0.021 0.071 0.036 0.1l0.029 0.067c0 0.013 0.020 0.053 0.040 0.080l0.040 0.053c0.020 0.013 0.040 0.053 0.060 0.080l0.040 0.053 0.053 0.053c0.013 0.017 0.013 0.040 0.040 0.040l0.080 0.056 0.053 0.040 0.013 0.019 14.627 9.773c0.219 0.16 0.5 0.217 0.76 0.217s0.52-0.080 0.76-0.24l14.877-9.875 0.069-0.077 0.044-0.060 0.053-0.080 0.040-0.067 0.040-0.093 0.021-0.069 0.040-0.103 0.020-0.060 0.040-0.107v-10c0-0.067 0-0.127-0.021-0.187l-0.019-0.060 0.059 0.004zM16.013 19.283l-4.867-3.253 4.867-3.256 4.867 3.253zM14.635 10.384l-5.964 3.987-4.817-3.221 10.781-7.187zM6.195 16.028l-3.443 2.307v-4.601zM8.671 17.695l5.964 3.987v6.427l-10.781-7.188 4.824-3.223zM17.387 21.681l5.965-3.973 4.817 3.227-10.783 7.187zM25.827 16.041l3.444-2.293v4.608zM23.353 14.388l-5.964-3.988v-6.44l10.78 7.187-4.816 3.22z"
	    }
	]

	const settingsPathCtx = ["path", {
        "d": "M11.366 22.564l1.291-1.807-1.414-1.414-1.807 1.291c-0.335-0.187-0.694-0.337-1.071-0.444l-0.365-2.19h-2l-0.365 2.19c-0.377 0.107-0.736 0.256-1.071 0.444l-1.807-1.291-1.414 1.414 1.291 1.807c-0.187 0.335-0.337 0.694-0.443 1.071l-2.19 0.365v2l2.19 0.365c0.107 0.377 0.256 0.736 0.444 1.071l-1.291 1.807 1.414 1.414 1.807-1.291c0.335 0.187 0.694 0.337 1.071 0.444l0.365 2.19h2l0.365-2.19c0.377-0.107 0.736-0.256 1.071-0.444l1.807 1.291 1.414-1.414-1.291-1.807c0.187-0.335 0.337-0.694 0.444-1.071l2.19-0.365v-2l-2.19-0.365c-0.107-0.377-0.256-0.736-0.444-1.071zM7 27c-1.105 0-2-0.895-2-2s0.895-2 2-2 2 0.895 2 2-0.895 2-2 2zM32 12v-2l-2.106-0.383c-0.039-0.251-0.088-0.499-0.148-0.743l1.799-1.159-0.765-1.848-2.092 0.452c-0.132-0.216-0.273-0.426-0.422-0.629l1.219-1.761-1.414-1.414-1.761 1.219c-0.203-0.149-0.413-0.29-0.629-0.422l0.452-2.092-1.848-0.765-1.159 1.799c-0.244-0.059-0.492-0.109-0.743-0.148l-0.383-2.106h-2l-0.383 2.106c-0.251 0.039-0.499 0.088-0.743 0.148l-1.159-1.799-1.848 0.765 0.452 2.092c-0.216 0.132-0.426 0.273-0.629 0.422l-1.761-1.219-1.414 1.414 1.219 1.761c-0.149 0.203-0.29 0.413-0.422 0.629l-2.092-0.452-0.765 1.848 1.799 1.159c-0.059 0.244-0.109 0.492-0.148 0.743l-2.106 0.383v2l2.106 0.383c0.039 0.251 0.088 0.499 0.148 0.743l-1.799 1.159 0.765 1.848 2.092-0.452c0.132 0.216 0.273 0.426 0.422 0.629l-1.219 1.761 1.414 1.414 1.761-1.219c0.203 0.149 0.413 0.29 0.629 0.422l-0.452 2.092 1.848 0.765 1.159-1.799c0.244 0.059 0.492 0.109 0.743 0.148l0.383 2.106h2l0.383-2.106c0.251-0.039 0.499-0.088 0.743-0.148l1.159 1.799 1.848-0.765-0.452-2.092c0.216-0.132 0.426-0.273 0.629-0.422l1.761 1.219 1.414-1.414-1.219-1.761c0.149-0.203 0.29-0.413 0.422-0.629l2.092 0.452 0.765-1.848-1.799-1.159c0.059-0.244 0.109-0.492 0.148-0.743l2.106-0.383zM21 15.35c-2.402 0-4.35-1.948-4.35-4.35s1.948-4.35 4.35-4.35 4.35 1.948 4.35 4.35c0 2.402-1.948 4.35-4.35 4.35z"
    }
]
	// Header Logo and Overview
	const mainNavCtx = ["nav", {"class": "navbar navbar-dark navbar-theme-primary px-4 col-12 d-lg-none"},
	    ["a", {"class": "navbar-brand me-lg-5", "href": "/"},
	        ["img", {
	                "class": "navbar-brand-dark",
	                "src": "/static/img/brand/light.svg",
	                "alt": "Volt logo",
	                "/": "/"
	            }
	        ],
	        ["img", {
	                "class": "navbar-brand-light",
	                "src": "/static/img/brand/dark.svg",
	                "alt": "Volt logo",
	                "/": "/"
	            }
	        ]
	    ],
	    ["div", {"class": "d-flex align-items-center"},
	        ["button", {
	                "class": "navbar-toggler d-lg-none collapsed",
	                "type": "button",
	                "data-bs-toggle": "collapse",
	                "data-bs-target": "#sidebarMenu",
	                "aria-controls": "sidebarMenu",
	                "aria-expanded": "false",
	                "aria-label": "Toggle navigation"
	            },
	            ["span", {"class": "navbar-toggler-icon"}]
	        ]
	    ]
	];


	// ok
	const genSideMenuSingleItem = function(itemId, clsAdd, itemHref, viewBox, iconPathCtx, labelName) {
		return ["li", {"id": itemId, "class": "nav-item "+clsAdd },
                ["a", {"href": itemHref, "class": "nav-link d-flex align-items-center"},
                    ["span", {"class": "sidebar-icon"},
                        ["svg", {
                                "class": "icon icon-xs me-2",
                                "fill": "currentColor",
                                "viewbox": viewBox,
                                "xmlns": "http://www.w3.org/2000/svg"
                            },
                            iconPathCtx
                        ]
                    ],
                    ["span", {"class": "sidebar-text"}, labelName]
                ]
            ]
	}

	const genMenuSeperator = function() {
		return ["li", {
	            "role": "separator",
	            "class": "dropdown-divider mt-4 mb-3 border-gray-700"
	        }
	    ]
	}

	const sideNavCtx = ["nav", {
        "id": "sidebarMenu",
        "class": "sidebar d-lg-block bg-gray-800 text-white collapse",
        "data-simplebar": "data-simplebar"
    },
    ["div", {"class": "sidebar-inner px-4 pt-3"},
        ["div", {
                "class": "user-card d-flex d-md-none align-items-center justify-content-between justify-content-md-center pb-4"
            },
            ["div", {"class": "collapse-close d-md-none"},
                ["a", {
                        "href": "#sidebarMenu",
                        "data-bs-toggle": "collapse",
                        "data-bs-target": "#sidebarMenu",
                        "aria-controls": "sidebarMenu",
                        "aria-expanded": "true",
                        "aria-label": "Toggle navigation"
                    },
                    ["svg", {
                            "class": "icon icon-xs",
                            "fill": "currentColor",
                            "viewbox": "0 0 20 20",
                            "xmlns": "http://www.w3.org/2000/svg"
                        },
                        ["path", {
                                "fill-rule": "evenodd",
                                "d": "M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z",
                                "clip-rule": "evenodd"
                            }
                        ]
                    ]
                ]
            ]
        ],
        ["ul", {"class": "nav flex-column pt-3 pt-md-0"},

            // (itemId, clsAdd, itemHref, viewBox, iconPathCtx, labelName)             
            genSideMenuSingleItem(eleIds['navMenuDashboardItem'],
            	"", "#/dashboard", "0 0 20 20", dashboardPathCtx, "Dashboard"),

            genSideMenuSingleItem(eleIds['navMenuRecentItem'],
            	"", "#/recent", "0 0 20 20", recentPathCtx, "Recent"),

            genSideMenuSingleItem(eleIds['navMenuAnalysisItem'],
            	"", "#/analysis", "0 0 32 32", analysisPathCtx, "Analysis"),

            genMenuSeperator(),

            genSideMenuSingleItem(eleIds['navMenuSystemItem'],
            	"", "#/settings", "0 0 32 32", settingsPathCtx, "Settings")

	        ]
	    ]
	]
	self.ctx = [mainNavCtx, sideNavCtx]

	self.initEvents = function() {
		
		$(".nav-item").click(function(){
			$('.nav-item').removeClass("active");
			$(this).addClass("active");

		})

		console.log("nav added events");
	}

	return self;

})();