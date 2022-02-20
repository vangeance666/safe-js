from typing import List
from dataclasses import dataclass, field
from analyzer.abstracts.feature import Feature

@dataclass
class JsFile:

	src: str = ""
	content: str = ""

	static_features: List[Feature] = field(default_factory=list)
	dynamic_features: List[Feature] = field(default_factory=list)

	# @classmethod	
	# def parse_element(cls, bs_element):
	# 	print("bs_element: ", bs_element)
		
	# 	if bs_element.has_attr('src'):			
	# 		return cls(bs_element['src'])
	# 	return cls()








