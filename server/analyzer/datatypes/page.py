from dataclasses import dataclass, field
from itertools import count
from typing import List, Optional

from analyzer.datatypes.js_file import JsFile
from bs4 import ResultSet


@dataclass
class Page:
	id: int = field(default_factory=count().__next__, init=False)
	src: str = field(default="")
	text: str = field(default="")

	script_elements: list = field(default_factory=list)

	internal_js_files: List[JsFile] = field(default_factory=list)
	external_js_files: List[JsFile] = field(default_factory=list)

	success: bool 		= field(default=False)
	parsed: bool 		= field(default=False)
	extracted: bool 	= field(default=False)
	saved: bool 		= field(default=False)
	is_analyzed: bool	= field(default=False)
