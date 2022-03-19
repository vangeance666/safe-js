from analyzer.core.utils import enumerate
from analyzer.abstracts import Feature

dynamic_features = enumerate(
    __file__, "analyzer.features.javascript.dynamic", globals(), Feature, as_dict=True
)

ioc_features

url_features 

active_url_features


