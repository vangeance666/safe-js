import glob
import json
import os
import shutil

from analyzer.core.exceptions import (DumpFormatError, ExecutionError,
                                      InvalidResourceError, InvalidUsageError)
from analyzer.core.utils import (format_js_file_save, recurs_create_folder,
                                 run_command, sha_256_str)

from analyzer.datatypes.box_js_result import BoxJsResult
from analyzer.datatypes.js_file import JsFile
from config import DYNAMIC_DUMP_FLDR


def onerror(func, path, exc_info):
    import stat
    # Is the error an access error?
    if not os.access(path, os.W_OK):
        os.chmod(path, stat.S_IWUSR)
        func(path)
    else:
        raise

# C:\Users\User\Documents\GitHub\safe-js\server\data\js_dynamic_results\page_cd5799acbcd45100ffea5ff03da25ef53e72678433193b23d627d8a42ef96844\js_file_0901879a02a24f54ab20c7641049f1b25a42fb91be805a82fbb86d031a330823\js_file_0901879a02a24f54ab20c7641049f1b25a42fb91be805a82fbb86d031a330823.results



class JsDynamicAnalyzer:

	RES_FLDR_EXT = ".results"

	CMD_BOX_JS = "box-js {} --no-shell-error --no-folder-exists --output-dir {}"

	ATTR_FILE_MAP = {
		"urls": "urls.json"
		, "active_urls": "active_urls.json"
		, "iocs":  "IOC.json"			
	}	

	def __init__(self):
		self._dump_folder = DYNAMIC_DUMP_FLDR 

	def cleanup(self):
		shutil.rmtree(self._dump_folder, ignore_errors=False)

	def _read_json_file(self, file_path) -> dict:
		try:
			with open(file_path):
				return json.load(f)
		except Exception as e:
			return None

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

	def parse_box_js_results(self, js_file: JsFile):

		if not js_file.dynamic_done:
			raise InvalidUsageError("Havent analyzed js_file yet")

		# print("js_file.dynamic_results_folder: ", js_file.dynamic_results_folder)
		if not js_file.dynamic_results_folder:			
			raise FileNotFoundError("JS File invalid box-js results folder")

		results_files = [f for f in os.listdir(js_file.dynamic_results_folder)]

		for attribute_name, file_name in self.ATTR_FILE_MAP.items():
			if file_name in results_files:
				try:
					with open(os.path.join(js_file.dynamic_results_folder, file_name)
						, 'r') as f:
						js_file.dynamic_results[attribute_name] = json.load(f)
						print("js_file.dynamic_results[attribute_name]: ", js_file.dynamic_results[attribute_name])
				except Exception as e:
					print(e)

		js_file.dynamic_results_parsed = True

	def _run_box_js(self, js_file: JsFile):

		if not os.path.exists(js_file.saved_path):
			print("js_file.saved_path: ", js_file.saved_path)
			raise InvalidUsageError("JS File not saved, Box-js only takes in files")
		
		if not js_file.page_src:
			print("js_file.page_src: ", js_file.page_src)
			raise InvalidResourceError("Js File not linked to any page.")

		# eval dump path by joining folder with js_file results path within page folder
		# Format for saving the js_file result: <DUMP_FOLDER>/<page_sha256>/<file_src_sha256>
		dump_dir = format_js_file_save(self._dump_folder, js_file) + "/" # add slash to make to dir
		recurs_create_folder(dump_dir) # Safe create folder if does not exists

		if not os.path.exists(dump_dir):
			raise FileNotFoundError("Box-JS Dump directory \"{}\" does not exist.".format(dump_dir))

		response = run_command(self.CMD_BOX_JS.format(js_file.saved_path, dump_dir))

		if response.stderr or response.returncode != 0:
			raise ExecutionError("Box JS returned error code of {}".format(response.stderr))

		res_folder = self._eval_latest_result_fldr(dump_dir, js_file)

		if not res_folder:
			raise InvalidResourceError("Cant evaluate and find box-js results folder.")
	
		js_file.dynamic_results_folder = os.path.join(dump_dir, res_folder)

		js_file.dynamic_done = True

	def run(self, js_file: JsFile):
		try:
			self._run_box_js(js_file)
		except Exception as e:
			print("Dynamic Extraction Error: ", e)
			js_file.dynamic_run_error = True					



