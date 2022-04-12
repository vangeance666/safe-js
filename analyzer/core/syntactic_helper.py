from typing import Callable

class ConditionsFactory:

	@staticmethod
	def element_func_call_condition(var_call_name) -> Callable:
		#E.g str.charCodeAt(idx)
		return lambda k: bool(k.type == "CallExpression" and k.callee.property.name == var_call_name)

	@staticmethod
	def add_event_listener_condition(event_name) -> Callable:
		# window.addEventListener("beforeunload", function(event) { /* ... */ });
		# event_name will be "beforeunload"
		def is_true(k) -> bool:
			if k.callee.property.type == "Identifier" \
				and k.callee.property.name == "addEventListener":
				
				return any(True for x in k.arguments 
					if x.type=="Literal" 
					and x.value==event_name)
			return False
		return is_true

	@staticmethod
	def on_event_assign_condition(on_event_name) -> Callable:
		# window.onbeforeunload = function(event) { /* ... */ };
		# on_event_name = "onbeforeunload"
		return lambda k: bool(
			k.left.type == "MemberExpression" 
			and k.left.property.type == "Identifier" 
			and k.left.property.name == on_event_name)

def parse_esprima(item, found_condition: Callable):

	counter = 0

	try:
		counter += int(found_condition(item))
	except:
		pass

	if isinstance(item, list):
		for obj in item:
			counter += parse_esprima(obj, found_condition)
	elif isinstance(item, object):
		try:
			for key in item.keys():
				counter += parse_esprima(getattr(item, key), found_condition)
		except:
			pass
	else:
		print("hmm managed to receive not dict or obj", )

	return counter