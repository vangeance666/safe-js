
import re
from analyzer.abstracts import IocFeature
from analyzer.datatypes.js_file import JsFile


class IocFolderCreate(IocFeature):
	_index_no: int = 8
	_name: str = "8_ioc_folder_create"	

	def _evaluate(self, js_file: JsFile):
		for ioc in js_file.dynamic_results.iocs:
			if ios['type'] == "FolderCreate":
				return 1		
		return 0

	def extract(self, js_file: JsFile):
		return self._evaluate(js_file)
	