$(function(){
	console.log("onload---")

	$('body').html(HTML(
		layout.nav.ctx,
		['div', {'id': ids['root'], 'class':'container-fluid'}, 
			['div', {'id': ids['rootBody'], 'class': 'container-fluid d-flex flex-column min-vh-100'}], // pages only change this
		],
		layout.footer.ctx
	));


	layout.nav.addEvents();
	
	HTML.route("", layout.pages.dashboard.display);
	HTML.route("dashboard", layout.pages.dashboard.display);
	HTML.route("recent", layout.pages.recent.display);
	HTML.route("analysis", layout.pages.analysis.display);

	HTML.route.go();
	

});