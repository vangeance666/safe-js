
class JsExtractionPatterns:

	@staticmethod
	def var_function(function_name, optional_params=False):
		if optional_params:
			return ".{1,}%s\(.*\)" %(function_name)
		return ".{1,}%s\(.+\)" %(function_name)

	@staticmethod
	def event(dot_call_str, event_listener_str):
		return ".+\.%s.+function|addEventListener\([\'\"]%s[\'\"]" %(dot_call_str, event_listener_str)

	@staticmethod
	def normal_function(name):
		return "%s\(.*\)" %(name)

	@staticmethod
	def files(extention):
		return ".+\.%s" %(extention)
