layout.pages.analysis = (function() {
	var self = {};


	var addEvents = function() {

	}

	self.display = function() {
		console.log("Analysis display toggled")

		$('#'+eleIds['rootBody']).html(HTML(self.ctx))

		addEvents();
	}

	return self;
})()
