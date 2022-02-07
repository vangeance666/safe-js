from analyzer.core.utils import enumerate
from analyzer.abstracts.feature import Feature

features = enumerate(
    __file__, "analyzer.features.javascript.static", globals(), Feature, as_dict=True
)



# import os

# buffer_template = """
# from dataclasses import dataclass
# from analyzer.abstracts.feature import Feature
# import re


# class {}(Feature):

# 	_index_no: int = {}
# 	_name: str = "{}"
# 	_var_type: type = int

# 	PATTERN = "{}"

# 	def _evaluate(self, js_buffer):
# 		return len(re.findall(self.PATTERN, js_buffer))

# 	def extract(self, js_buffer):
# 		return self._evaluate(js_buffer)

# 	@property
# 	def index_no(self):
# 		return self._index_no

# 	@property
# 	def name(self):
# 		return self._name	

# 	@property
# 	def var_type(self):
# 		return self._var_type

# """

# def replacer(s, newstring, index, nofail=False):
#     # raise an error if index is outside of the string
#     if not nofail and index not in range(len(s)):
#         raise ValueError("index outside given string")

#     # if not erroring, but the index is still not in the correct range..
#     if index < 0:  # add it to the beginning
#         return newstring + s
#     if index > len(s):  # add it to the end
#         return s + newstring

#     # insert the new string between "slices" of the original
#     return s[:index] + newstring + s[index + 1:]


# def format_class_name(str_input):
# 	ret = str_input


# 	for i, x in enumerate(ret):
# 		if i == 0:
# 			ret = replacer(ret, x.upper(), i)
# 		elif ret[i] == '_':
# 			ret = replacer(ret, ret[i+1].upper(), i+1)
# 			# ret[i+1] = x.upper()

# 	ret = ret.replace("_", '')
# 	return ret



# X = ["func_split_count", "func_onerrorcount", "func_func_set_attribute_count", "func_window_location_count", "func_char_at_count", "func_log_count", "func_decode_count", "func_tostring_count", "func_math_random_count", "func_charcodeat_count", "event_onbeforeunload_count", "event_onload_count", "event_onunload_count", "event_onbeforeload_count", "event_onmouseover_count", "event_dispatchevent_count", "event_fireevent_count", "keyword_function_count", "keyword_wscript_count", "char_digits_count", "char_encoded_count", "char_backslash_count", "char_pipe_count", "char_percent_count", "char_left_parenthesis_count", "char_right_parenthesis_count", "char_comma_count", "char_hash_count", "char_plus_count", "char_dot_count", "char_single_quote_count", "char_open_bracket_count", "char_close_bracket_count", "char_open_brace_count", "char_close_brace_count", "page_js_files_count", "page_php_files_count"]

# print(len(X))

# for x in range(2,len(X)+1):
# 	file_path = os.path.join(str(x), os.getcwd(), str(x)+"_"+X[x-1]+".py")

# 	class_name = format_class_name(X[x-1])
# 	name = X[x-1]
# 	index_no = x
# 	pattern = ""

# 	with open(file_path, 'w') as f:
# 		f.write(buffer_template.format(class_name, index_no, name, pattern))






