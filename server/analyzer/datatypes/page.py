from typing import List, Optional
from dataclasses import dataclass, field
from analyzer.datatypes.js_file import JsFile
from bs4 import ResultSet

@dataclass(order=True)
class Page:
	src: str = field(default="")
	text: str = field(default="")

	script_elements: list = field(default_factory=list)

	internal_js_files: List[JsFile] = field(default_factory=list)
	external_js_files: List[JsFile] = field(default_factory=list)

	success: bool 	= field(default=False)
	parsed: bool 	= field(default=False)
	extracted: bool = field(default=False)
	saved: bool 	= field(default=False)