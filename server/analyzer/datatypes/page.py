from typing import List, Optional
from dataclasses import dataclass, field
from analyzer.datatypes.js_file import JsFile

@dataclass(order=True)
class Page:
	url: str = field(default="")
	internal_js_files: List[JsFile] = field(default_factory=list)
	external_js_files: List[JsFile] = field(default_factory=list)

	success: bool = field(default=False)