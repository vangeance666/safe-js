from dataclasses import dataclass, field
from itertools import count
from typing import List, Optional

from analyzer.datatypes.js_file import JsFile
from app.models.processing_status import ProcessingStatus
from bs4 import ResultSet


@dataclass
class Page:
	id: int = field(default_factory=count().__next__, init=False)
	src: str = field(default="")
	text: str = field(default="")
	
	status: ProcessingStatus = field(default=ProcessingStatus.PENDING)

	script_elements: list = field(default_factory=list)

	internal_js_files: List[JsFile] = field(default_factory=list)
	external_js_files: List[JsFile] = field(default_factory=list)

	error_reason: str = field(default="-")
	
	crawl_success: bool 		= field(default=False)
	elements_parsed: bool 		= field(default=False)
	js_elements_extracted: bool = field(default=False)
	saved: bool 				= field(default=False)
	is_analyzed: bool			= field(default=False)
	features_extracted: bool 	= field(default=False)
	is_predicted: bool 			= field(default=False)
