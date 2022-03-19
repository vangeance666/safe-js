from dataclasses import dataclass, field
from typing import List


@dataclass
class BoxJsResult:

	# analysis_logs: str = ""
	# snippets: list = field(default_factory=list)
	urls: list = field(default_factory=list)
	# active_urls: list = field(default_factory=list)
	# resources: list = field(default_factory=list)
	iocs: list = field(default_factory=list)

# Need to flatten when saving to csv
