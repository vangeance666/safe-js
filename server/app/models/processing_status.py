from enum import Enum, auto


class ProcessingStatus(Enum):
	ERROR = auto()
	PENDING = auto()
	CRAWLING = auto()
	ANALYZING = auto()
	EXTRACTING_FEATURES = auto()
	PREDICTING = auto()
	DONE = auto()
