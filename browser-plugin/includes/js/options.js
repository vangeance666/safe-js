console.log("options.js loaded----");


function saveOptions(e) {
	e.preventDefault();

	browser.storage.local.set({
		"serverDetails": {"urlValue": document.querySelector("#options-server").value}
	});
}

function restoreOptions() {

	function setServerUrl(data) {
		if (data.serverDetails) {
			document.querySelector("#options-server").value = data.serverDetails.urlValue || "Nothing";
		} else {
			console.log("data server details not set yet.");
		}
	}

	function onError(error) {
		console.log(`Error: ${error}`);
	}

	let getting = browser.storage.local.get("serverDetails");
	getting.then(setServerUrl, onError);
}


$(function() {
	restoreOptions();
	$("#save-button").click(saveOptions);
});
// document.addEventListener("DOMContentLoaded", restoreOptions);

// document.querySelector("#save-button").addEventListener("click", saveOptions);
