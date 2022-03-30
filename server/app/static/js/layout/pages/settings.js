layout.pages.settings = (function() {
	var self = {};


	var addEvents = function() {

	}

	self.display = function() {
		console.log("Settings display toggled")

		$('#'+ids['rootBody']).html(HTML(self.ctx))

		addEvents();
	}

	return self;
})()
