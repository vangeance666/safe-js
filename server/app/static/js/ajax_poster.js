
var ajaxPoster = function(postUrl, dictMsg) {
	var res;

	$.ajax({
	    type: "POST",
	    contentType: "application/json",
	    url: postUrl,
	    data: JSON.stringify(dictMsg)
	    // url: "api/upload/",
	    // data: JSON.stringify({"mode":"upload", "message": "fuckyou"})
	    
	}).done(function (e) {				
		res = e;
		console.log(e)
	});

	console.log("outside res: ", res);
	return res;
}();