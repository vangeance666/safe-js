from analyzer.abstracts import (Feature, IOCFeature, UrlsFeatures, ActiveUrlsFeature)

from analyzer.core.utils import enumerate

dynamic_features = enumerate(
    __file__, "analyzer.features.javascript.dynamic"
    , globals(), Feature, as_dict=True
)

ioc_features = enumerate(
    __file__, "analyzer.features.javascript.dynamic"
    , globals(), IOCFeature, as_dict=True
)

url_features  = enumerate(
    __file__, "analyzer.features.javascript.dynamic"
    , globals(), UrlsFeatures, as_dict=True
)

active_url_features = enumerate(
    __file__, "analyzer.features.javascript.dynamic"
    , globals(), ActiveUrlsFeature, as_dict=True
)


# benign_urls = [
# 	"xsite.singaporetech.edu.sg"
# 	, "google.com"
# ]

# malign_urls = [
# 	"example.virus.com"
# 	, "example2.virus.com"
# ]




