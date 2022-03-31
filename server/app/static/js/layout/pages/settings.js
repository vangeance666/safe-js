layout.pages.settings = (function() {
	let self = {};


	const initEvents = function() {
		layout.banner.setBannerPath(["Page", "Settings"])
		layout.banner.setBannerHeader("Settings")
		layout.banner.setBannerDescription("Change configurations")
		layout.banner.setActionRightButton("")

		
	}

	self.display = function() {
		console.log("Settings display toggled")

		$('#'+eleIds['rootBody']).html(HTML(self.ctx))

		initEvents();
	}

	return self;
})()
