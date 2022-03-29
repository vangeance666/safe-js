
import re
from analyzer.abstracts import IocFeature
from analyzer.datatypes.js_file import JsFile


class IocFileRead(IocFeature):
	_index_no: int = 6
	_name: str = "6_ioc_file_read"	

	def _evaluate(self, js_file: JsFile):
		for ioc in js_file.dynamic_results.iocs:
			if ios['type'] == "FileRead":
				return 1		
		return 0

	def extract(self, js_file: JsFile):
		return self._evaluate(js_file)
	