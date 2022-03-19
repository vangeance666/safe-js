from analyzer.core.utils import enumerate
from analyzer.abstracts import Feature

static_features = enumerate(
    __file__, "analyzer.features.javascript.static", globals(), Feature, as_dict=True
)