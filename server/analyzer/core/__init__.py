from analyzer.features.javascript.dynamic import (active_url_features,
                                                  ioc_features, url_features)
from analyzer.features.javascript.static import static_features

STATIC_MAPPING: list = [
	{"attr_name": "all", "features_dict": static_features}
]
	

BOX_JS_MAPING: list = [
	{"attr_name": "iocs", "file_name": "IOC.json", "features_dict": ioc_features}
	, {"attr_name": "urls", "file_name": "urls.json", "features_dict": url_features}
	, {"attr_name": "active_urls", "file_name": "active_urls.json", "features_dict": active_url_features}
]
