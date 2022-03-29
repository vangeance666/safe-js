import atexit
import itertools
import sys
from dataclasses import asdict

import esprima
from analyzer.controllers.features_controller import FeaturesController
from analyzer.controllers.page_controller import PageController
from analyzer.controllers.analysis_controller import AnalysisController
from analyzer.controllers.results_controller import ResultsController

from analyzer.core.dataset_generator import DatasetGenerator


from app import create_app

dataset_generator = DatasetGenerator()

page_controller = PageController()
features_controller = FeaturesController()
analysis_controller  = AnalysisController()
results_controller = ResultsController()

if __name__ == '__main__':

	
	# pass

	pages = results_controller.load_pages()
	dataset_generator.pages_to_csv(pages, "yoyo.csv")

	# if pages is None:


	# 	# if 

	# 	# if not pages:
	# 	# 	print("No saved pages results found")
		

	# pages = page_controller.extract_pages(["https://developer.mozilla.org/en-US/docs/Web/API/WindowEventHandlers/onbeforeunload"])

	# # # print("saving js files---")
	# page_controller.save_js_files(pages)

	# # with AnalysisController() as analysis_controller:
	# analysis_controller.analyze_pages_js_files(pages)
	# # with FeaturesController() as features_controller:
	# features_controller.extract_pages_features(pages)
		

	# for p in pages:
	# 	for i, j in enumerate(p.internal_js_files):
	# 		print("Internal--", str(i), str(j.src))
	# 		print(j.static_features)

	# 	for i, j in enumerate(p.external_js_files):
	# 		print("External--", str(i), str(j.src))
	# 		print(j.dynamic_features)

	# print('---saving pages---')
	# results_controller.save_pages(pages)
	# print("finish")



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
