from typing import List
from dataclasses import dataclass, field
from analyzer.abstracts.feature import Feature

@dataclass
class JsFile:

	src: str = ""
	content: str = ""

	static_features: dict = field(default_factory=dict)
	dynamic_features: dict = field(default_factory=dict)

	# @classmethod	
	# def parse_element(cls, bs_element):
	# 	print("bs_element: ", bs_element)
		
	# 	if bs_element.has_attr('src'):			
	# 		return cls(bs_element['src'])
	# 	return cls()








