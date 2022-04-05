
import re
from analyzer.abstracts import IocFeature
from analyzer.datatypes.js_file import JsFile


class IocUrlFetch(IocFeature):
	_index_no: int = 1
	_name: str = "1_ioc_url_fetch"	

	def _evaluate(self, js_file: JsFile):
		print("js_file.dynamic_results.iocs: ", js_file.dynamic_results.iocs)

		for ioc in js_file.dynamic_results.iocs:
			print("ioc: ", ioc)
			if ioc['type'] == "UrlFetch":
				return 1		
		return 0

	def extract(self, js_file: JsFile):
		return self._evaluate(js_file)
	