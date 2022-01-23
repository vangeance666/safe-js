$(function(){
	$('body').html(HTML(
		layout.nav.ctx,
		['div', {'id': ids['root'], 'class':'container-fluid'}, 
			['div', {'id': ids['bodyRoot'], 'class': 'container-fluid'}], // pages only change this
		],
		layout.footer().ctx

	));


	HTML.route("upload/", layout.pages.upload.display);
	HTML.route("overview/", layout.pages.overview.display);
	HTML.route("results/", layout.pages.results.display);
	HTML.route("modelstatistics/", layout.pages.modelStatistics.display);


	layout.nav.addEvents();
	
	layout.pages.upload.display();

	console.log("loaded main")

});