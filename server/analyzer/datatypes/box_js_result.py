from dataclasses import dataclass, field
from typing import List

@dataclass
class BoxJsResult:
	urls: dict = field(default_factory=dict)
	active_urls: dict = field(default_factory=dict)
	iocs: dict = field(default_factory=dict)