
from analyzer.abstracts import Feature, IocFeature, UrlsFeatures, ActiveUrlsFeature

from analyzer.core.utils import enumerate_modules


ioc_features = enumerate_modules(__file__, "analyzer.features.javascript.dynamic", globals(), IocFeature, as_dict=True)
url_features  = enumerate_modules(__file__, "analyzer.features.javascript.dynamic", globals(), UrlsFeatures, as_dict=True)

active_url_features = enumerate_modules(__file__, "analyzer.features.javascript.dynamic", globals(), ActiveUrlsFeature, as_dict=True)


dynamic_features = ioc_features