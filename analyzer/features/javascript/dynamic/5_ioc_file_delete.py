
import re
from analyzer.abstracts import IocFeature
from analyzer.datatypes.js_file import JsFile


class IocFileDelete(IocFeature):
	_index_no: int = 5
	_name: str = "5_ioc_file_delete"	

	def _evaluate(self, js_file: JsFile):
		for ioc in js_file.dynamic_results.iocs:
			if ioc['type'] == "FileDelete":
				return 1		
		return 0

	def extract(self, js_file: JsFile):
		return self._evaluate(js_file)
	