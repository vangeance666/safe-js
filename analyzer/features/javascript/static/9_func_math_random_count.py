import re

from analyzer.abstracts import Feature
from analyzer.abstracts import Feature
from analyzer.core.syntactic_helper import ConditionsFactory, parse_esprima
from analyzer.datatypes.js_file import JsFile

class FuncMathRandomCount(Feature):

    _index_no: int = 9
    _name: str = "func_math_random_count"
    _var_type: type = int

    PATTERN = ""

    def _evaluate(self, js_file: JsFile) -> int:
        return js_file.text.count("Math.random()")

    def extract(self, js_file: JsFile):
        return self._evaluate(js_file)

    
