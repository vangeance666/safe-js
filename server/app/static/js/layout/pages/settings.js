layout.pages.settings = (function() {
	var self = {};


	var addEvents = function() {

	}

	self.display = function() {
		console.log("Settings display toggled")

		$('#'+eleIds['rootBody']).html(HTML(self.ctx))

		// addEvents();
	}

	return self;
})()
