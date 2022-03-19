import os

from analyzer.core.utils import (format_js_file_save, recurs_create_folder,
                                 run_command, sha_256_str)
from analyzer.datatypes.box_js_result import BoxJsResult
from analyzer.datatypes.js_file import JsFile
from config import DYNAMIC_DUMP_FLDR


class JsDynamicAnalyzer:

	RES_FLDR_EXT = ".results"

	CMD_BOX_JS = "box-js {} --no-shell-error --no-folder-exists --output-dir {}"	

	def __init__(self):
		self._dump_folder = DYNAMIC_DUMP_FLDR 

		self.FILE_FUNC_MAP = {
			"IOC.json" : self._parse_iocs
			, "urls.json" : self._parse_urls
			, "active_urls.json" : self._parse_active_urls
		}

	def _eval_latest_result_fldr(self, results_folder: str, js_file: JsFile) -> str:

		start = ''.join(["js_file_", sha_256_str(js_file.src)])
		L = len(start)
		N = -abs(len(self.RES_FLDR_EXT))

		res = []

		for f in os.listdir(results_folder):
			if f[N:] == self.RES_FLDR_EXT and f[:L] == start:
				val = f.replace(self.RES_FLDR_EXT, '')
				if len(val) != L:
					res.append(val[L+1:])

		if not res:
			return ''.join([start, self.RES_FLDR_EXT])

		return ''.join([start, '.', str(max(res)), self.RES_FLDR_EXT])

	def _parse_iocs(self, dynamic_results: BoxJsResult):
		pass

	def _parse_urls(self, dynamic_results: BoxJsResult):
		pass

	def _parse_active_urls(self, dynamic_results: BoxJsResult):
		pass
		
	def parse_result(self, js_file: JsFile) -> BoxJsResult:

		if not js_file.dynamic_done or not js_file.dynamic_dump_folder:
			raise Exception("JS File dynamic analysis not done yet.")

		results_files = [f for f in os.listdir(js_file.dynamic_dump_folder)]

		for file_name, func in self.FILE_FUNC_MAP.items():
			if file_name in results_files:
				func(js_file.dynamic_results)

	def analyze(self, js_file: JsFile):

		if not os.path.exists(js_file.saved_path):
			raise Exception("JS File save path does not exist.")
		
		if not js_file.page_src:
			raise Exception("Js File not linked to any page.")

		# eval dump path by joining folder with js_file results path within page folder
		# Format for saving the js_file result: <DUMP_FOLDER>/<page_sha256>/<file_src_sha256>
		dump_dir = format_js_file_save(self._dump_folder, js_file) + "/" # add slash to make to dir
		recurs_create_folder(dump_dir) # Safe create folder if does not exists

		if not os.path.exists(dump_dir):
			raise Exception("Box-JS Dump directory {} does not exist." % dump_dir)


		# save_point = [f for f in os.listdir(dump_dir)]

		try:
			command = self.CMD_BOX_JS.format(js_file.saved_path, dump_dir)
			print("command: ", command)
			response = run_command(command)

			if response.stderr or response.returncode != 0:
				raise Exception("Box JS execution error.")

			res_folder = self._eval_latest_result_fldr(dump_dir, js_file)
			print("res_folder: ", res_folder)

			if not res_folder:
				raise Exception("Cant evaluate and find box-js results folder.")
		
			js_file.dynamic_dump_folder = os.path.join(dump_dir, res_folder)
	
		except Exception as e:
			raise e

		js_file.dynamic_done = True
