from analyzer.controllers.features_controller import FeaturesController
from analyzer.controllers.page_controller import PageController


from dataclasses import asdict

import esprima

from app import create_app

if __name__ == '__main__':

	P = PageController()
	C = FeaturesController()

	pages = P.extract_pages(["https://developer.mozilla.org/en-US/docs/Web/API/WindowEventHandlers/onbeforeunload"])
	

	print(len(pages))
	print(type(pages[0].script_elements))

	C.extract_urls_features(pages)

	