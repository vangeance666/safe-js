from analyzer.core.utils import enumerate_packages
from analyzer.abstracts import Feature

static_features = enumerate_packages(
    __file__, "analyzer.features.javascript.static", globals(), Feature, as_dict=True
)