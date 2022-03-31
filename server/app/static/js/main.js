$(function(){
	console.log("onload---")

	$('body').html(HTML(
		layout.nav.ctx,
		["div", {"class": "container-fluid", "id": eleIds['root']},
		    ["main", {"id": eleIds['rootMain'], "class": "content"},
		    	layout.banner.ctx,
		    	["div", {"class": "d-flex flex-column min-vh-100",
		            "id": eleIds['rootBody']}
		        ],
		        layout.footer.ctx
		        
		    ]
		    
		]
		
	));

	layout.nav.addEvents();
		
	// HTML.route("", layout.pages.dashboard.display);
	HTML.route("dashboard", layout.pages.dashboard.display);
	HTML.route("recent", layout.pages.recent.display);
	HTML.route("analysis", layout.pages.analysis.display);
	HTML.route("settings", layout.pages.settings.display);

	HTML.route.go(":dashboard");
});