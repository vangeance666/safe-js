
import os

import re

def cw2us(x): # capwords to underscore notation
    return re.sub(r'(?<=[a-z])[A-Z]|(?<!^)[A-Z](?=[a-z])',
        r"_\g<0>", x).lower(  )

def us2mc(x): # underscore to mixed-case notation
    return re.sub(r'_([a-z])', lambda m: (m.group(1).upper(  )), x)


OUT = """
import re
from analyzer.abstracts import IOCFeature
from analyzer.datatypes.js_file import JsFile


class {}:
	_index_no: int = {}
	_name: str = "{}"	

	def _evaluate(self, js_file: JsFile):
		return 1

	def extract(self, js_file: JsFile):
		if not js_file.dynamic_results.iocs:
			return 0, 0
		return 1, self._evaluate(js_file)
"""

TO_PUT = ["UrlFetch","NewResource","FileWrite","Run","FileDelete","FileRead","RegRead","FolderCreate"]


# for x in TO_PUT:

# 	print(cw2us(x))
# for i in range(len(TO_PUT)):
# 	class_name = 'Ioc'+TO_PUT[i]
# 	print("class_name: ", class_name)
# 	name = '_'.join([str(i+1), 'ioc', cw2us(TO_PUT[i])])
# 	file_name = name+'.py'
# 	index = str(i+1)

# 	with open(file_name, 'w') as f:
# 		f.write(OUT.format(class_name, index, name))

	# with open("", 'w') as f:
DIR = "C:\\Users\\User\\Documents\\GitHub\\safe-js\\server\\analyzer\\features\\javascript\\static"
for file in os.listdir(DIR):

	if file not in ['__pycache__']:
		path = os.path.join(DIR, file)


		with open(path, 'r') as f:
			data = f.read()
			print("data: ", data)

			res = re.findall("\sdef\sextract\(self, js_file\: JsFile\)\:\n\t\t.*", data)
			print("res: ", res)
			

		break
