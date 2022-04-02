worker.status = (function() {
	const self = {};

	const queryServerStatus = function() {
		setTimeout(function() {
	        $.ajax({
	        	url: "heartbeat/",
	        	type: 'GET'
	        })
	        .done(function(e) {
	        	if (e.status === "healthy") {
	        		queryServerStatus();  // Repeat this function again.
	        	}
				else 
					layout.pages.error.display()
	        })
	        .fail(function(e) {
	        	
	        	
	        	layout.pages.error.display();
	        });

	    }, 30000);
	}

	self.start = function() {
		
		queryServerStatus();
	}

	return self;	
})();