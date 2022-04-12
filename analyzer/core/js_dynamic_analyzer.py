import json
import os
import shutil
from pathlib import Path

from analyzer.core import BOX_JS_MAPING
from analyzer.core.exceptions import (DumpFormatError, ExecutionError,
                                      InvalidResourceError, InvalidUsageError)
from analyzer.core.js_features_extractor import JsFeaturesExtractor
from analyzer.core.utils import (format_js_file_save, recurs_create_folder,
                                 run_command, sha_256_str)
from analyzer.datatypes.box_js_result import BoxJsResult
from analyzer.datatypes.js_file import JsFile


class JsDynamicAnalyzer:

	name = "JsDynamicAnalyzer"

	RES_FLDR_EXT = ".results"

	CMD_BOX_JS = "box-js {} --no-shell-error --no-folder-exists --output-dir {}"

	ATTR_FILE_MAP = {
		"urls": "urls.json"
		, "active_urls": "active_urls.json"
		, "iocs":  "IOC.json"			
	}

	def __init__(self, dump_folder: str):
		self._dump_folder = dump_folder
		self._box_js_mapping = BOX_JS_MAPING

	def cleanup(self):
		if os.path.exists((self._dump_folder)):
			shutil.rmtree(self._dump_folder, ignore_errors=False)

	def _run_box_js(self, js_file: JsFile, output_dir) -> None:
		
		response = run_command(self.CMD_BOX_JS.format(js_file.saved_path, output_dir))

		if response.stderr or response.returncode != 0:
			raise ExecutionError("Box JS returned error code of {}".format(response.stderr))

		res_folder = self._latest_box_js_folder(output_dir, js_file)

		if not res_folder:
			raise InvalidResourceError("Cant evaluate and find box-js results folder.")
	
		js_file.dynamic_results_folder = os.path.join(output_dir, res_folder)
		
		js_file.dynamic_done = True

		
	def _latest_box_js_folder(self, output_dir: str, js_file: JsFile) -> str:

		folder_name = os.path.basename(js_file.saved_path)

		for path in sorted(
			iterable=Path(output_dir).iterdir()
			, key=os.path.getmtime
			, reverse=True):

			base_name = os.path.basename(path)
			if base_name.startswith(folder_name) \
				and base_name.endswith(self.RES_FLDR_EXT):

				return str(path)

		return ""

	def parse_box_js_results(self, js_file: JsFile) -> None:

		if not js_file.dynamic_done:
			raise InvalidUsageError("Havent analyzed js_file yet")

		if not js_file.dynamic_results_folder:			
			raise FileNotFoundError("JS File invalid box-js results folder")

		for mapping in self._box_js_mapping:
			artifact_path = os.path.join(js_file.dynamic_results_folder
				, mapping['file_name'])

			if os.path.exists(artifact_path):
				with open(artifact_path, 'r', encoding='utf8') as f:
					data = json.loads(f.read())
					setattr(js_file.dynamic_results
						, mapping['attr_name']
						, data if data else "JSON Error")

		js_file.dynamic_results_parsed = True

	def run(self, js_file: JsFile) -> None:

		if not os.path.exists(js_file.saved_path):
			
			raise InvalidUsageError("JS File not saved, Box-js only takes in files")

		dump_folder = format_js_file_save(self._dump_folder, js_file.page_id, js_file.id) + "/" # add slash to make to dir
		recurs_create_folder(dump_folder) # Safe create folder if does not exists

		if not os.path.exists(dump_folder):
			raise FileNotFoundError("Box-JS Dump directory \"{}\" failed to create.".format(dump_folder))

		self._run_box_js(js_file, dump_folder)	
		self.parse_box_js_results(js_file)
