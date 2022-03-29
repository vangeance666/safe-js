
import re
from analyzer.abstracts import IOCFeature
from analyzer.datatypes.js_file import JsFile


class IocRun:
	_index_no: int = 4
	_name: str = "4_ioc_run"	

	def _evaluate(self, js_file: JsFile):
		for ioc in js_file.dynamic_results.iocs:
			if ios['type'] == "Run":
				return 1		
		return 0

	def extract(self, js_file: JsFile):
		return self._evaluate(js_file)
