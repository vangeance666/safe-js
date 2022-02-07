import sys
from analyzer.core.utils import get_file_buffer
from analyzer.features.javascript.static import features


class FeaturesController:
	
	def __init__(self):
		self._features = features

	def get_static_features(self, js_path=None) -> dict:
		ret = {}

		js_buffer = self._get_js_buffer(js_path)

		if not js_buffer:
			return ret

		for x in self._features:

			x_obj = self._features[x]()
			ret[x_obj.name] = x_obj.extract(js_path)

		return ret

