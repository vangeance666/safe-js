layout.pages.analysis = (function() {
	let self = {};

	const submitUrlBtnPath = ["path", {
	        "d": "M14 18h4v-8h6l-8-8-8 8h6zM20 13.5v3.085l9.158 3.415-13.158 4.907-13.158-4.907 9.158-3.415v-3.085l-12 4.5v8l16 6 16-6v-8z"
	    }
	]

	const initEvents = function() {
		layout.banner.setBannerPath(["Page", "Analysis"])
		layout.banner.setBannerHeader("Analysis")
		layout.banner.setBannerDescription("View results details of submission")

		layout.banner.setActionRightButton(eleIds["analysisSubmitBtn"],
		 "", submitUrlBtnPath, "0 0 32 32", "Submit URL")
	}

	self.display = function() {
		console.log("Analysis display toggled")

		$('#'+eleIds['rootBody']).html(HTML(self.ctx))
		

		initEvents();
	}

	return self;
})()
