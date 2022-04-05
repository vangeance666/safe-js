worker.status = (function() {
	const self = {};

	const queryServerStatus = function() {
		setTimeout(function() {
	        $.ajax({
	        	url: "heartbeat/",
	        	type: 'GET'
	        })
	        .done(function(e) {
	        	// console.log("Done e: ", e);
	        	if (e.status === "Healthy") {
	        		queryServerStatus();  // Repeat this function again.
	        	}
				else 
					layout.pages.error.display()
	        })
	        .fail(function(e) {
	        	// console.log("Fail e: ", e);

	        	
	        	
	        	layout.pages.error.display();
	        });

	    }, 5000);
	}

	self.start = function() {
		
		queryServerStatus();
	}

	return self;	
})();