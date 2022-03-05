from app import create_app
from analyzer.controllers.features_controller import FeaturesController
from analyzer.core.syntactic_helper import *
from analyzer.extractors.page_parser import PageParser

import esprima

from dataclasses import asdict
 	
if __name__ == '__main__':

	# page_parser = PageParser()
	# page_details = page_parser.get_page_details("https://developer.mozilla.org/en-US/docs/Web/API/WindowEventHandlers/onbeforeunload")
	# print(dir(page_details))
	# 
	# for x in page_details.internal_js_files:
	# 	print(x)
	# print(asdict(page_details))
	# print("hehe: ", hehe)

	# C = FeaturesController()
	# C.extract_urls_features(["https://developer.mozilla.org/en-US/docs/Web/API/WindowEventHandlers/onbeforeunload"])
	# print("C.get_static_features(): ", C.get_static_features())
	
	malware_path = "C:\\Users\\User\\Documents\\GitHub\\safe-js\\server\\analyzer\\careful.txt"
	yo = "C:\\Users\\User\\Documents\\GitHub\\Malware_Classification_Identification\\app\\static\\js\\init.js"


	testing_path ="C:\\Users\\User\\Documents\\GitHub\\Malware_Classification_Identification\\app\\static\\js\\layout\\pages\\model_statistics.js"
	with open(testing_path) as f:
		buff = f.read()

	# X = """var hehebongesh = function({
	# 	console.log("yo");
	# })
	# """

	S = """
	var addEvents = function() {

		$('select').on('change', function() {
			selectedModel = this.value;
		  // alert( this.value );
		});

        $('#'+ids['modelStatisticsBtn']).click(function(){
        	// Based on select value, retrieve data from python and populate graphs
        	populateModelGraphs();

        });

		console.log("added page model statistics events")
	}
	"""

	test2 = """
	var totn_string = 'TechOnTheNet';

	console.log(totn_string.charCodeAt());
	"""

	test3 = """
	window.addEventListener("beforeunload", function(event) { /* ... */ });
	window.onbeforeunload = function(event) { /* ... */ };
	"""
	import inspect

	P = esprima.parse("Element.setAttribute(name, value);")

	condition = lambda k: bool(k.type == "CallExpression" and k.callee.property.name == "charCodeAt")

	counter = parse_esprima(P.body, ConditionsFactory.on_event_assign_condition("onbeforeunload"))
	print("counter: ", counter)

	 
	print(P.body)