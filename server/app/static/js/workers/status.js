worker.status = (function() {
	const self = {};

	const queryServerStatus = function() {
		setTimeout(function() {
	        $.ajax({
	        	url: "heartbeat/",
	        	type: 'GET'
	        })
	        .done(function(e) {
	        	console.log("Heartbeat sucess func")
	        	console.log("e: ", e);
	        	if (e.status === "healthy") {
	        		console.log("Server is healthy")
	        		queryServerStatus();  // Repeat this function again.
	        	}
				else 
					layout.pages.error.display()
	        })
	        .fail(function(e) {
	        	console.log("Heartbeat fail func")
	        	console.log("e: ", e);
	        	layout.pages.error.display();
	        });

	    }, 30000);
	}

	self.start = function() {
		console.log("started worker status")
		queryServerStatus();
	}

	return self;	
})();