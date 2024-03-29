
import re
from analyzer.abstracts import IocFeature
from analyzer.datatypes.js_file import JsFile


class IocNewResource(IocFeature):
	_index_no: int = 2
	_name: str = "2_ioc_new_resource"	

	def _evaluate(self, js_file: JsFile):
		for ioc in js_file.dynamic_results.iocs:
			if ioc['type'] == "NewResource":
				return 1		
		return 0

	def extract(self, js_file: JsFile):
		return self._evaluate(js_file)
	