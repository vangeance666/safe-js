from typing import List
from dataclasses import dataclass
from analyzer.datatypes.jsfile import JsFile

class Page:
	url: str
	js_files: List[JsFile]