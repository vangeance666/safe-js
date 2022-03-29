
import re
from analyzer.abstracts import IOCFeature
from analyzer.datatypes.js_file import JsFile


class IocFolderCreate:
	_index_no: int = 8
	_name: str = "8_ioc_folder_create"	

	def _evaluate(self, js_file: JsFile):
		return 1

	def extract(self, js_file: JsFile):
		if not js_file.dynamic_results.iocs:
			return 0, 0
		return 1, self._evaluate(js_file)
