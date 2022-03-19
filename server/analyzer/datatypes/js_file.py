from analyzer.abstracts import Feature
from analyzer.datatypes.box_js_result import BoxJsResult

from dataclasses import dataclass, field
from typing import List



@dataclass(order=True)
class JsFile:

	src: str = ""
	text: str = ""

	success: bool = False #Determine if text variable parsed success

	is_saved: bool = False

	dynamic_done: bool = False

	page_src: str = "" # To identify which page is it from (Parent)
	# rel_path: str = ""
	saved_path: str = ""

	dynamic_results_folder: str = ""
	dynamic_results: BoxJsResult = field(default_factory=BoxJsResult)

	syntactic_extract: list = field(default_factory=list)

	static_features: dict = field(default_factory=dict)
	dynamic_features: dict = field(default_factory=dict)

