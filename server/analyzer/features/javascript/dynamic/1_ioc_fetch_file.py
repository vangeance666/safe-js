import re

from analyzer.abstracts import IOCFeature
from analyzer.datatypes.js_file import JsFile


class IOCFetchFile(IOCFeature):

	_index_no: int = 1
	_name: str = "ioc_fetch_file"
	_var_type: type = int

	_description: str = "Evaluate if js file fetches a file"

	def _evaluate(self, js_file: JsFile) -> int:
		return 1

	def extract(self, js_file: JsFile):
		return self._evaluate(js_file)

# C:\Users\User\Documents\GitHub\safe-js\server\data\js_dynamic_results\page_cd5799acbcd45100ffea5ff03da25ef53e72678433193b23d627d8a42ef96844\js_file_0901879a02a24f54ab20c7641049f1b25a42fb91be805a82fbb86d031a330823\js_file_0901879a02a24f54ab20c7641049f1b25a42fb91be805a82fbb86d031a330823.results
