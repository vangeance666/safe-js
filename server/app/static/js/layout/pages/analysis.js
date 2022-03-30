layout.pages.analysis = (function() {
	var self = {};


	var addEvents = function() {

	}

	self.display = function() {

		$('#'+ids['rootBody']).html(HTML(self.ctx))

		addEvents();
	}

	return self;
})()
