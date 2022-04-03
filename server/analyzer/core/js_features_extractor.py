import os

from analyzer.core.dataset_generator import DatasetGenerator
from analyzer.core.exceptions import InvalidUsageError
from analyzer.core.utils import cw2us, us2mc
from analyzer.datatypes.js_file import JsFile
from analyzer.features.javascript.dynamic import (active_url_features,
                                                  ioc_features, url_features)
from analyzer.features.javascript.static import static_features

from analyzer.core.utils import format_js_file_save

class JsFeaturesExtractor:

	BOX_JS_MAPING: list = [
		{"attr_name": "iocs", "file_name": "IOC.json", "features_dict": ioc_features}
		, {"attr_name": "urls", "file_name": "urls.json", "features_dict": url_features}
		, {"attr_name": "active_urls", "file_name": "active_urls.json", "features_dict": active_url_features}
	]

	STATIC_MAPPING: list = [
		{"attr_name": "all", "features_dict": static_features}
	]

	def __init__(self, dynamic_dump_folder: str):
		self._dynamic_dump_folder = dynamic_dump_folder

	def _parse_features(self, features: dict, js_file: JsFile) -> dict:

		ret = {}

		for key in features:

			feature_obj = features[key]()

			attr_name = cw2us(features[key].__name__)

			try:
				ret[attr_name] = (1, feature_obj.extract(js_file))
			except Exception as e:
				print(e)
				ret[attr_name]  = (0,0) # 0 To represent error				

		return ret

	def extract_dynamic_features(self, js_file: JsFile):

		if js_file.dynamic_run_error:
			raise InvalidUsageError("Unable to extract dynamic features since dynamic analysis has errors")

		if not js_file.dynamic_done or not js_file.dynamic_results_parsed:
			raise InvalidUsageError("Not analyzed with Box-jS yet, cant extract features")

		if not js_file.dynamic_results_folder:
			raise InvalidUsageError("Invalid dynamic results folder")

		print("js_file.dynamic_results_folder: ", js_file.dynamic_results_folder)

		# Dunnid to parse the folder again?
		for mapping in self.BOX_JS_MAPING:

			to_find_file = os.path.join(js_file.dynamic_results_folder, mapping['file_name'])

			if not os.path.exists(to_find_file):
				print("to_find_file does not exists: ", to_find_file)
				js_file.dynamic_features[mapping['attr_name']] = DatasetGenerator.no_feature_found_row(mapping['features_dict'])
				continue

			js_file.dynamic_features[mapping['attr_name']] = self._parse_features(mapping['features_dict'], js_file)

		js_file.dynamic_features_done = True

	def extract_static_features(self, js_file: JsFile):

		if js_file.static_run_error:
			raise InvalidUsageError("Unable to extract static features since static analysis has errors")

		if not js_file.synthetic_done:
			raise InvalidUsageError("Synthetic details not extracted")

		if not js_file.text:
			raise ValueError("Invalid JS text attribute.")

		for mapping in self.STATIC_MAPPING:
			js_file.static_features[mapping['attr_name']] = self._parse_features(mapping['features_dict'], js_file)

		js_file.static_features_done = True










