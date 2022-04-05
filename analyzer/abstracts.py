from abc import ABC, abstractmethod, abstractproperty


class Feature(ABC):

	has_error: bool = False

	@property
	def index_no(self):
		return self._index_no

	@property
	def name(self):
		return self._name	

	@property
	def var_type(self):
		return self._var_type

	@abstractmethod
	def extract(self, js_file):
		raise NotImplementedError("Need to override this")

class DynamicFeature(Feature):
	pass


class IocFeature(DynamicFeature):
	pass


class UrlsFeatures(DynamicFeature):
	pass


class ActiveUrlsFeature(DynamicFeature):
	pass

