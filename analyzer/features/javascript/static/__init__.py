from analyzer.core.utils import enumerate_modules
from analyzer.abstracts import Feature

static_features = enumerate_modules(
    __file__, "analyzer.features.javascript.static", globals(), Feature, as_dict=True
)