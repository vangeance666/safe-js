from enum import Enum, auto


class ProcessingStatus(Enum):
	ERROR = auto()
	PENDING = auto()
	CRAWLING = auto()
	CRAWLED = auto()
	ANALYZING = auto()
	ANALYZED = auto()
	PREDICTING = auto()
	PREDICTED = auto()
	DONE = auto()
