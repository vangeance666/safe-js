import os

from analyzer.datatypes.js_file import JsFile
from analyzer.features.javascript.dynamic import ioc_features, url_features, active_url_features
print("active_url_features: ", active_url_features)
print("url_features: ", url_features)
print("ioc_features: ", ioc_features)
from analyzer.features.javascript.static import static_features


class JsFeaturesExtractor:

	def __init__(self):

		self._static_features: dict = static_features

	def _parse_features(self, features, js_file: JsFile) -> dict:

		ret = {}

		for key in features:
			feature_obj = features[key]()
			ret[feature_obj.name] = feature_obj.extract(js_file)

		return ret

	def extract_dynamic_features(self, js_file: JsFile):

		if not js_file.dynamic_done:
			raise Exception("Box-JS Analysis for this jsfile not done yet")

		js_file.dynamic_features["iocs"] = self._parse_features(ioc_features, js_file)
		js_file.dynamic_features["urls"] = self._parse_features(url_features, js_file)
		js_file.dynamic_features["active_urls"] = self._parse_features(active_url_features, js_file)

		js_file.dynamic_features_done = True

	def extract_static_features(self, js_file: JsFile):

		if not js_file.synthetic_done:
			raise Exception("Synthetic details not extracted yet")

		if not js_file.text:
			raise ValueError("Invalid JS text attribute.")		

		js_file.static_features["all"] = self._parse_features(static_features, js_file)

		# print("Extracting static features for :", js_file.src)
		# for x in self._static_features:
		# 	print("Currently extracting: ", x)
		# 	x_obj = self._static_features[x]()
		# 	js_file.static_features["all"] = x_obj.extract(js_file)

		js_file.static_features_done = True
