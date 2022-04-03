import ast
import atexit
import itertools
import json
import os
import pickle
import shutil
import sys
import threading
import time
from collections import deque
from dataclasses import asdict
from multiprocessing import Pool

import esprima
import jsbeautifier
import requests
import uvicorn
from analyzer.controllers.analysis_controller import AnalysisController
from analyzer.controllers.features_controller import FeaturesController
from analyzer.controllers.page_controller import PageController
from analyzer.controllers.results_controller import ResultsController
from analyzer.core.dataset_generator import DatasetGenerator
from analyzer.datatypes.js_file import JsFile
from analyzer.datatypes.page import Page
from app.threads.analyzer_thread import AnalyzerThread
from samples import benign_urls, malign_urls

page_controller = PageController()
features_controller = FeaturesController()
results_controller = ResultsController()

dataset_generator = DatasetGenerator()
page_controller = PageController()
features_controller = FeaturesController()
analysis_controller  = AnalysisController()
results_controller = ResultsController()

# from app.platform_controller import PlatformController
# platform_controller = PlatformController()
# platform_controller.save_all()
# atexit.register(platform_controller.cleanup)


class A(threading.Thread):
	def __init__(self, pending_queue):
		super().__init__()
		self._pending_queue = pending_queue

	def run(self):

		for x in self._pending_queue:
			print(x)
		return 


def analyze_one_url(url) -> Page:
	page = Page(url)
	page_controller.crawl_details(page)
	page_controller.save_js_file(page)

	with AnalysisController() as analysis_controller:
		analysis_controller.analyze_page_js_files(page)

	for js_file in itertools.chain(page.internal_js_files, page.external_js_files):
		try:
			features_controller.extract_static_features(js_file)
			print("Finished static features for {}".format(js_file.src))
		except Exception as e:
			print(e)
		try:
			features_controller.extract_dynamic_features(js_file)
			print("Finished dyanmic features for {}".format(js_file.src))						
		except Exception as e:
			print(e)
	return page



def do_smth(D):
	try:

		url = D if D.startswith('http') else ('http://'+D)

		r = requests.get(url)
		# return ' '.join([D, str(r.status_code)])
		if r.status_code == 200:
			return str(url)
		# if r.status_code != 200:
		# 	return ' '.join([url, str(r.status_code)])

		return None
	except Exception as e:
		return None
		return e

def gen_list():
	for x in benign_urls:
		yield x

if __name__ == "__main__":


	ok_files = []

	with Pool(processes=32) as pool:
		for res in pool.imap_unordered(do_smth, gen_list()):
			if res is not None:
				print("ok res: ", res)
				ok_files.append(res)
				

	with open("okay_urls.txt", 'w') as f:
		for file in ok_files:
			f.write(str(file)+'\n')


	# path = "C:\\Users\\User\\Documents\\GitHub\\safe-js\\server\\data\\js_dynamic_results"
	# if os.path.exists(path):
	# #     shutil.rmtree(path)

	# analyzed = []
	# pending = deque([])
	
	# pending.append(Page("https://stackoverflow.com/questions/66770132/python-uniqe-integer-for-dataclass"))

	# w = AnalyzerThread(pending, analyzed, "True")

	# w.start()

	# x = {"settings":{"userProfile":{"openGraphAPIKey":"4a307e43-b625-49bb-af15-ffadf2bda017"},"userMessaging":{"showNewFeatureNotice":""},"tags":{},"subscriptions":{"defaultBasicMaxTrueUpSeats":250,"defaultFreemiumMaxTrueUpSeats":50,"defaultMaxTrueUpSeats":1000},"snippets":{"renderDomain":"stacksnippets.net","snippetsEnabled":""},"site":{"allowImageUploads":"","enableImgurHttps":"","enableUserHovercards":"","forceHttpsImages":"","styleCode":""},"questions":{"enableQuestionTitleLengthLiveWarning":"","maxTitleSize":150,"questionTitleLengthStartLiveWarningChars":50},"intercom":{"appId":"inf0secd","hostBaseUrl":"https://stacksnippets.net"},"paths":{},"monitoring":{"clientTimingsAbsoluteTimeout":30000,"clientTimingsDebounceTimeout":1000},"mentions":{"maxNumUsersInDropdown":50},"markdown":{"enableTables":""},"legal":{"oneTrustConfigId":"c3d9f1e3-55f3-4eba-b268-46cee4c6789c"},"flags":{"allowRetractingCommentFlags":"","allowRetractingFlags":""},"elections":{"opaVoteResultsBaseUrl":"https://www.opavote.com/results/"},"comments":{},"accounts":{"currentPasswordRequiredForChangingStackIdPassword":""}}}
	# x = str(x)
	# x = x.replace('\t','')
	# x = x.replace('\n','')
	# x = x.replace(',}','}')
	# x = x.replace(',]',']')
	# x = x.replace('\'', '\"')
	# print("x: ", x)


	# data = ast.literal_eval(json.dumps(x))
	# print("data: ", data)
	
	# x = json.dumps(x)
	# x = jsbeautifier.beautify(str(x))
	# x = json.dumps(x)

	# res = esprima.parse(json.dumps(data))
	# print("res: ", res)
	# with open("C:\\Users\\User\\Documents\\GitHub\\safe-js\\server\\save\\errors\\internal_js_2.txt", 'r') as f:
	#   data= json.loads(f.read())
	#   print("data: ", data)
	#   	
	# pass
	
	# for i in range(3):
	#   a = A(pending_queue=[str(i) for i in range(100)])
	#   print(dir(a))
		# a.start()
	# results = platform_controller.fetch_js_file_details(0, 1)

	# print(platform_controller.fetch_dashboard_details())

	# uvicorn.run("app.main:app", host="0.0.0.0", port=8090, reload="True") 

	# pages = results_controller.load_pages()


	# for page in pages:
	#   for js_file in itertools.chain(page.internal_js_files, page.external_js_files):
	#       print("src", js_file.src)
	#       print(page.id, js_file.src)
	# print(pages[1].src)
	# for j in pages[1].internal_js_files:
	#   print(j)

	# if pages is None:

	# dataset_generator.pages_to_csv(pages, "yoyo.csv")



	#   # if 

	#   # if not pages:
	#   #   print("No saved pages results found")
		


	# pages = page_controller.extract_pages(["https://developer.mozilla.org/en-US/docs/Web/API/WindowEventHandlers/onbeforeunload", "https://stackoverflow.com/questions/66770132/python-uniqe-integer-for-dataclass"])


	# # # print("saving js files---")
	# page_controller.save_js_files(pages)

	# # with AnalysisController() as analysis_controller:
	# analysis_controller.analyze_pages_js_files(pages)
	# # with FeaturesController() as features_controller:
	# features_controller.extract_pages_features(pages)
		

	# for p in pages:
	#   for i, j in enumerate(p.internal_js_files):
	#       print("Internal--", str(i), str(j.src))
	#       print(j.static_features)

	#   for i, j in enumerate(p.external_js_files):
	#       print("External--", str(i), str(j.src))
	#       print(j.dynamic_features)

	# print('---saving pages---')
	# results_controller.save_pages(pages)
