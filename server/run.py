import ast
import atexit
import itertools
import json
import os
import pickle
import shutil
import signal
import sys
import threading
import time
from collections import deque
from dataclasses import asdict
from multiprocessing import Pool

import esprima
import jsbeautifier
import pandas as pd
import requests
import uvicorn
from analyzer.controllers.analysis_controller import AnalysisController
from analyzer.controllers.features_controller import FeaturesController
from analyzer.controllers.inference_controller import InferenceController
from analyzer.controllers.page_controller import PageController
from analyzer.controllers.results_controller import ResultsController
from analyzer.core.dataset_generator import DatasetGenerator
from analyzer.core.page_parser import PageParser
from analyzer.core.url_validator import UrlValidator
from analyzer.datatypes.js_file import JsFile
from analyzer.datatypes.page import Page
from app.threads.analyzer_thread import AnalyzerThread
from app.threads.cleaner_thread import CleanerThread
from app.threads.crawler_thread import CrawlerThread
from app.threads.inference_thread import InferenceThread
from config import DONE_PAGES_SAVE_PATH
from samples import benign_urls, malign_urls

page_controller = PageController()
features_controller = FeaturesController()
results_controller = ResultsController()

dataset_generator = DatasetGenerator()
page_controller = PageController()
features_controller = FeaturesController()
analysis_controller  = AnalysisController()
results_controller = ResultsController()

inference_controller = InferenceController()

url_validator = UrlValidator()
page_parser = PageParser()

# from app.platform_controller import PlatformController
# platform_controller = PlatformController()
# platform_controller.save_all()

def analyze_malign_df_row(row):
	page = Page(row.url.strip())
	page.text = str(row.content).strip()
	page.crawl_success = True
	page_parser.parse_page_elements(page)

	try:
		page_parser.parse_js_content(page)

		page_controller.save_js_file(page)

		with AnalysisController() as analysis_controller:
			for js_file in itertools.chain(page.internal_js_files, page.external_js_files):
				analysis_controller.run_static_analysis(js_file)
				analysis_controller.run_dynamic_analysis(js_file)
				features_controller.extract_all_features(js_file)
	except Exception as e:
		print("analyze_malign_df_row error: ", e)


	return page

# To parse those Benign urls
def analyze_one_url(url) -> Page:
	page = Page(url)

	try:
		page_controller.crawl_details(page)
	except Exception as e:
		print("First crawl try: ", e)
		try:
			page.url = page.url.replace("http://", "https://")
			page_controller.crawl_details(page)
		except Exception as e2:
			print("Second try still fail, ", e)

	page_controller.save_js_file(page)

	with AnalysisController() as analysis_controller:
		for js_file in itertools.chain(page.internal_js_files, page.external_js_files):
			analysis_controller.run_static_analysis(js_file)
			analysis_controller.run_dynamic_analysis(js_file)
			features_controller.extract_all_features(js_file)

	# 	analysis_controller.analyze_page_js_files(page)
	# for js_file in itertools.chain(page.internal_js_files, page.external_js_files):
	# 	try:
	# 		features_controller.extract_static_features(js_file)
	# 		print("Finished static features for {}".format(js_file.src))
	# 	except Exception as e:
	# 		print(e)
	# 	try:
	# 		features_controller.extract_dynamic_features(js_file)
	# 		print("Finished dyanmic features for {}".format(js_file.src))						
	# 	except Exception as e:
	# 		print(e)
	return page

# To parse those js samples 
def analyze_one_js_file(index: str, js_file_path) -> JsFile:
	js_file = JsFile()

	js_file.id = index #Dirty way to not trigger error
	js_file.page_id = index #Dirty way to not trigger error
	js_file.is_saved = True	 #Since manual approach not thru normal flow

	js_file.saved_path = js_file_path	

	with open(js_file_path, 'r') as f:
		js_file.text = f.read()	

	with AnalysisController() as analysis_controller:
		analysis_controller.run_static_analysis(js_file)
		analysis_controller.run_dynamic_analysis(js_file)
		# Must use like that cause analysis controller will delete everything after that 
		features_controller.extract_all_features(js_file)

	return js_file


MALWARE_FOLDER = "C:\\Users\\User\\Downloads\\js-malicious-dataset-master\\js-malicious-dataset-master"

# atexit.register(save_pages_info)
# signal.signal(signal.SIGTERM, save_pages_info)
# signal.signal(signal.SIGINT, save_pages_info)

def test_threads_url():
	analyzed = []
	pending_pages = deque([])	
	pending_pages.append(Page("http://xsite.singaporetech.edu.sg"))
	# pending_pages.append(Page("https://stackoverflow.com/questions/66770132/python-uniqe-integer-for-dataclass"))
	to_run = True
	thead_lock = threading.Lock()

	crawler_thread = CrawlerThread(thead_lock, pending_pages,analyzed, to_run)
	analyzer_thread = AnalyzerThread(thead_lock, pending_pages, analyzed, to_run)
	cleaner_thread = CleanerThread(thead_lock, pending_pages,analyzed,  to_run)
	inference_thread = InferenceThread(thead_lock, pending_pages,analyzed,  to_run)

	crawler_thread.start()
	analyzer_thread.start()
	cleaner_thread.start()
	inference_thread.start()

if __name__ == "__main__":
	# test_threads_url()
	uvicorn.run("app.main:app", host="0.0.0.0", port=8090, reload="True") 

	# js_file = analyze_one_js_file(1, "C:\\Users\\User\\Documents\\GitHub\\safe-js\\server\\careful.txt")

	# with open("js_file_temp.pickle", 'wb') as f:
	# 	pickle.dump(js_file, f)

	# with open()
	# inference_controller.predict("c-7.npz", js_file)
	# print("js_file: ", js_file)

	# a = A("hehe")
	# b = A("haha")
	# c = A("yo")
	# d = deque([a,b,c])

	# print("d: ", d)

	# for i, x in enumerate(d):
	# 	if x.name == "haha":
	# 		del d[i]
	# 		break
	
	# print(b.name)

	# print(url_validator.check("xsite.singaporetech.edu.sg"))

	# with open("C:\\Users\\User\\Downloads\\done_ok.txt",'r') as f1:

	# 	with open("replaced.txt", 'w') as f2:

	# 		for x in f1.readlines():
	# 			f2.write(x.split("ok res:  ")[1])


	# DATASET_PATH = "C:\\Users\\User\\Downloads\\Dataset of Malicious and Benign Webpages\\testdata\\Webpages_Classification_test_data.csv"

	
	# CSV_SAVE_PATH = "ok_malign_pk_laptop1.csv"
	# dataset_generator.write_header_csv(CSV_SAVE_PATH)

	# df = pd.read_csv(DATASET_PATH, names=["index","url","url_len","ip_add","geo_loc","tld","who_is","https","js_len","js_obf_len","content", "label"])
	# df = df.loc[df['label'] == "bad"]
	
	# to_put_in_csv = []
	# for i, row in df.iloc[1:].iterrows():
	# 	# print("row: ", row)
	# 	# print(row.url, row.content, row.label)
		
	# 	page = analyze_malign_df_row(row)

	# 	# for js_file in itertools.chain(page.internal_js_files, page.external_js_files):
	# 	# 	print(js_file)
	# 	to_put_in_csv.append(page)

	# 	if i % 2 == 0:
	# 		dataset_generator.append_pages_to_csv(to_put_in_csv, CSV_SAVE_PATH)
	# 		del to_put_in_csv
	# 		to_put_in_csv = []

	# print("Finish")


	# to_put_in_csv = []
	# csv_save_path = "ok_malign_pk_laptop.csv"
	# dataset_generator.write_header_csv(csv_save_path)
	# i= 0
	# for url in get_benign_urls():
	# 	print("Cycle: ", str(i))
	# 	print("url: ", url)
	# 	page = analyze_one_url(url)
	# 	# for js_file in itertools.chain(page.internal_js_files, page.external_js_files):
	# 	# print(js_file)
	# 	to_put_in_csv.append(page)

	# 	if i % 2 == 0:
	# 		dataset_generator.append_pages_to_csv(to_put_in_csv, csv_save_path)
	# 		del to_put_in_csv
	# 		to_put_in_csv = []
			
	# 	i += 1

	
	# from pathlib import Path
	# paths = sorted(Path("C:\\Users\\User\\Documents\\GitHub\\safe-js\\server").iterdir(), key=os.path.getmtime, reverse=True)

	# for x in paths:
	# 	print(os.path.basename(x))
	# 	print(dir(x))
	# 	print(type(x))
	# 	print(str(x))
	# 	break
	# print("paths: ", paths)
	# js_file = analyze_one_js_file(1,"C:\\Users\\User\\Downloads\\samples\\test1.js")
	# print("js_file: ", js_file)

	# print("dynamic_results: ", js_file.dynamic_results)
	# print("dynamic_features: ", js_file.dynamic_features)





	# ok_files = []

	# with Pool(processes=32) as pool:
	# 	for res in pool.imap_unordered(do_smth, gen_list()):
	# 		if res is not None:
	# 			print("ok res: ", res)
	# 			ok_files.append(res)
				

	# with open("okay_urls.txt", 'w') as f:
	# 	for file in ok_files:
	# 		f.write(str(file)+'\n')


	# path = "C:\\Users\\User\\Documents\\GitHub\\safe-js\\server\\data\\js_dynamic_results"
	# if os.path.exists(path):
	# #     shutil.rmtree(path)
	
	# #####################
	


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
	#   a = A(pending_pages=[str(i) for i in range(100)])
	#   print(dir(a))
		# a.start()
	# results = platform_controller.fetch_js_file_details(0, 1)
	# print(platform_controller.fetch_dashboard_details())

	# max_val = max([1,2,3,4,56,7,]+[1,5,5,7,5,1],  default=0)
	# print("max_val: ", max_val)
	# uvicorn.run("app.main:app", host="0.0.0.0", port=8090, reload="False") 

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
	# for page in pages:
	# 	for js_file in itertools.chain(page.internal_js_files, page.external_js_files):
	# 		with AnalysisController() as analysis_controller:
	# 			analysis_controller.run_static_analysis(js_file)
	# 			analysis_controller.run_dynamic_analysis(js_file)
	# 			features_controller.extract_all_features(js_file)
		

	# for p in pages:
	#   for i, j in enumerate(p.internal_js_files):
	#       print("Internal--", str(i), str(j.src))
	#       print(j.static_features)

	#   for i, j in enumerate(p.external_js_files):
	#       print("External--", str(i), str(j.src))
	#       print(j.dynamic_features)

	# print('---saving pages---')
	# results_controller.save_pages(pages, DONE_PAGES_SAVE_PATH)
