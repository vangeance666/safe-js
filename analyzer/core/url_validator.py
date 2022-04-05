import requests
from urllib.parse import urlparse


class FormatError(Exception):
	pass

class ConnectionError(Exception):
	pass

class UrlValidator:


	def __init__(self):
		pass

	def _check_format(self, url):
		try:
			result = urlparse(url)
			print("result: ", result)
			return all([result.scheme, result.netloc])
		except Exception as e:
			raise e

	def _test_connection(self, url):
		try:
			r = requests.get(url, allow_redirects=True)
			return r.ok and r.status_code == 200
		except Exception as e:
			raise e

	def check(self, url):
		if not self._check_format(url):
			raise FormatError("Invalid URL format, ensure proper scheme and netloc")

		if not self._test_connection(url):
			raise ConnectionError("Connection failure error for {}".format(url))		
		return True