import os

from analyzer.core.exceptions import InvalidUsageError
from analyzer.core.utils import cw2us, us2mc
from analyzer.datatypes.js_file import JsFile
from analyzer.features.javascript.dynamic import (active_url_features,
                                                  ioc_features, url_features)
from analyzer.features.javascript.static import static_features


class JsFeaturesExtractor:

	def __init__(self):

		self._static_features: dict = static_features

	def _parse_features(self, features, js_file: JsFile) -> dict:

		ret = {}

		for key in features:
			feature_obj = features[key]()

			try:
				ret[features[key].__name__] = (1, feature_obj.extract(js_file))
			except Exception as e:
				print(e)
				ret[features[key].__name__]  = (0,0) # 0 To represent error				

		return ret

	def extract_dynamic_features(self, js_file: JsFile):

		if not js_file.dynamic_done:
			raise InvalidUsageError("Not analyzed with Box-jS yet, cant extract features")

		

		js_file.dynamic_features["iocs"] = self._parse_features(ioc_features
			, js_file)

		js_file.dynamic_features["urls"] = self._parse_features(url_features
			, js_file)

		js_file.dynamic_features["active_urls"] = self._parse_features(active_url_features
			, js_file)		

		js_file.dynamic_features_done = True

	def extract_static_features(self, js_file: JsFile):

		if not js_file.synthetic_done:
			raise InvalidUsageError("Synthetic details not extracted yet.")

		if not js_file.text:
			raise ValueError("Invalid JS text attribute.")		

		js_file.static_features["all"] = self._parse_features(static_features, js_file)

		js_file.static_features_done = True
