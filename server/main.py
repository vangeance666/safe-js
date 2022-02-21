from app import create_app
from analyzer.controllers.features_controller import FeaturesController

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
	with open(malware_path) as f:
		buff = f.read()

	# X = """var hehebongesh = function({
	# 	console.log("yo");
	# })
	# """

	P = esprima.parse(buff)
	print(P)
	# print("P: ", type(P))
	print(dir(P.body))
	print(type(P.body))
	# print(P.body)
	# 
	 
