import atexit
import itertools
import sys
from dataclasses import asdict

import esprima
from analyzer.controllers.features_controller import FeaturesController
from analyzer.controllers.page_controller import PageController
from analyzer.controllers.results_controller import ResultsController
from app import create_app

page_controller = PageController()
# features_controller = FeaturesController()
results_controller = ResultsController()



if __name__ == '__main__':

	# import os

	# for f in os.listdir("c:\\Users"):
	# X = "C:\\Users\\User\\Documents\\GitHub\\safe-js\\server\\data\\js_dynamic_results\\page_cd5799acbcd45100ffea5ff03da25ef53e72678433193b23d627d8a42ef96844\\js_file_0901879a02a24f54ab20c7641049f1b25a42fb91be805a82fbb86d031a330823\\js_file_0901879a02a24f54ab20c7641049f1b25a42fb91be805a82fbb86d031a330823.results\\"
	# for f in os.listdir(X):


	# 	print(f)

	pages = results_controller.load_pages()

	# if not pages:
	# 	print("No saved pages results found")
	

	pages = page_controller.extract_pages(["https://developer.mozilla.org/en-US/docs/Web/API/WindowEventHandlers/onbeforeunload"])
	

	# # print("saving js files---")	
	page_controller.save_js_files(pages)

	with FeaturesController() as features_controller:
		features_controller.extract_pages_features(pages)
	
	# results_controller.save_pages(pages)




	# for p in pages:
	# 	# for j in p.external_js_files:
	# 	# 	print("Ext--")
	# 	# 	print(j.static_features)

	# 	for i,j in enumerate(p.internal_js_files):
	# 		print("Internal--",str(i))

	# 		print(j.src, j.text.encode(), j.static_features)
	# 		print("\n\n\n----")
	
	# for p in pages:
	# 	for j in itertools.chain(p.internal_js_files, p.external_js_files):
	# 		j.text = ""


	# for p in pages:

	# 	for j in itertools.chain(p.internal_js_files, p.external_js_files):
	# 		try:
	# 			print(j.__dict__)
	# 		except Exception as e:
	# 			print(e)
	# 		continue



