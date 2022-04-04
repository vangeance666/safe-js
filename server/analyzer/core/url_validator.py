import requests
from urllib.parse import urlparse, auto

from enum import Enum


class UrlStatus(Enum):
	WRONG_FORMAT = auto()
	CONNECTION_FAIL = auto()
	OK = auto()

class UrlValidator:


	def __init__(self):
		pass

	def _check_format(self, url) -> bool:
	    try:
	        result = urlparse(x)
	        return all([result.scheme, result.netloc])
	    except:
	        return False

	def _test_connection(self, url) -> bool:
		try:
			r = requests.head(url)
			print(r.text)
			return r.ok and r.status_c
		except:
			return False

	def check(self, url):

		if not self._check_format(url):
			raise FormatError("Invalid URL format")

		if not self._test_connection(url):
			raise ConnectionError("Connection failure error for {}".format(url))

		return True