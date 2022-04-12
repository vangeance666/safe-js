import hashlib
import importlib
import inspect
import math
import os
import pkgutil
import re
import subprocess

from analyzer.datatypes.js_file import JsFile


def enumerate_modules(dirpath, module_prefix, namespace, class_, attributes={}, as_dict=False):
    
    if os.path.isfile(dirpath):
        dirpath = os.path.dirname(dirpath)

    for _, module_name, _ in pkgutil.iter_modules([dirpath], module_prefix+"."):
        try:
            importlib.import_module(module_name)
        except ImportError as e:
            raise e

    subclasses = class_.__subclasses__()[:]

    modules = []
    while subclasses:
        subclass = subclasses.pop(0)
        subclasses.extend(subclass.__subclasses__())

        if not subclass.__module__.startswith(module_prefix):
            continue

        namespace[subclass.__name__] = subclass
        for key, value in attributes.items():
            setattr(subclass, key, value)

        modules.append(subclass)

    if as_dict:
        ret = {}
        for plugin in modules:
            plugin_module = plugin.__module__[len(module_prefix) + 1:]
            ret[plugin_module] = plugin
        return ret

    return sorted(modules, key=lambda x: x.__name__.lower())

def get_file_buffer(file_path):
    with open(file_path, 'r', encoding='utf8') as f:
        return f.read()

def entropy(string):
    "Calculates the Shannon entropy of a string"

    # get probability of chars in string
    prob = [ float(string.count(c)) / len(string) for c in dict.fromkeys(list(string)) ]

    # calculate the entropy
    entropy = - sum([ p * math.log(p) / math.log(2.0) for p in prob ])

    return entropy

def sha_256_str(text) -> str:
    return hashlib.sha256(text.encode()).hexdigest()

def md5_str(text) -> str:
    return hashlib.sha256(text.encode()).hexdigest()

def save_file(file_path, text) -> bool:
    try:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, 'w', encoding="utf8") as f:
            f.write(text)
    except Exception as e:
        print(e)
        return False
    return True

def recurs_create_folder(folder: str):
    os.makedirs(os.path.dirname(folder), exist_ok=True)


def run_command(command):
    # print("command: ", command)
    try:
        return subprocess.run(command, shell=True, stdout=subprocess.PIPE)
    except Exception as e:
        raise e

def format_js_file_save(dump_folder: str, page_id, js_file_id) -> str:
    return os.path.join(dump_folder
        , "page_"+str(page_id)
        , "js_"+str(js_file_id))


def cw2us(x): # capwords to underscore notation
    return re.sub(r'(?<=[a-z])[A-Z]|(?<!^)[A-Z](?=[a-z])',
        r"_\g<0>", x).lower(  )

def us2mc(x): # underscore to mixed-case notation
    return re.sub(r'_([a-z])', lambda m: (m.group(1).upper(  )), x)


    