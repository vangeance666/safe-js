from dataclasses import dataclass, field
from itertools import count
from typing import List

from analyzer.abstracts import Feature
from analyzer.datatypes.box_js_result import BoxJsResult


@dataclass(order=True)
class JsFile:
	id: int = field(default_factory=count().__next__, init=False)

	page_id: int = -1
	
	src: str = ""
	text: str = ""

	success: bool = False #Determine if text variable parsed success

	is_saved: bool = False

	synthetic_done: bool = False
	static_run_error: bool = False
	static_done: bool = False

	page_src: str = "" # To identify which page is it from (Parent)
	saved_path: str = ""

	dynamic_done: bool = False
	dynamic_run_error: bool = False

	dynamic_results_folder: str = ""
	dynamic_results_parsed: bool = False
	dynamic_results: BoxJsResult = field(default_factory=BoxJsResult)

	syntactic_extract: list = field(default_factory=list)

	static_features: dict = field(default_factory=dict)
	static_features_done: bool = False
	static_features_error: bool = False

	dynamic_features: dict = field(default_factory=dict)
	dynamic_features_done: bool = False
	dynamic_features_error: bool = False

	model_predicted: bool = False
	malign_percent: float = 0.0

	def get_text(self) -> str:
		if self.saved_path:
			with open(self.saved_path, 'r') as f:
				return f.read()

		return ""
