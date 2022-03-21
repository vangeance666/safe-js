import hashlib
import importlib
import inspect
import math
import os
import pkgutil
import subprocess

from analyzer.datatypes.js_file import JsFile


def enumerate(dirpath, module_prefix, namespace, class_, attributes={}, as_dict=False):
    
    if os.path.isfile(dirpath):
        dirpath = os.path.dirname(dirpath)

    for _, module_name, _ in pkgutil.iter_modules([dirpath], module_prefix+"."):
        try:
            importlib.import_module(module_name)
        except ImportError as e:
            raise Exception("Failed to import, "+str(e))

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

def format_js_file_save(folder: str, js_file: JsFile) -> str:
    return os.path.join(folder
        , "page_"+sha_256_str(js_file.page_src)
        , "js_file_"+sha_256_str(js_file.src))


"C:\\Users\\User\\Documents\\GitHub\\safe-js\\server\\save\\pages\\cd5799acbcd45100ffea5ff03da25ef53e72678433193b23d627d8a42ef96844\\87f23dbb35cf254215afee3a56defbbdd57f431f0e5ac3e8410b9a4881ea9028",
"C:\\Users\\User\\Documents\\GitHub\\safe-js\\server\\save\\pages\\cd5799acbcd45100ffea5ff03da25ef53e72678433193b23d627d8a42ef96844\\c3a79c720747cd44fab04ded2a448939af68a1121883d57d9c4c7da07a09bbe2",



"C:\\Users\\User\\Documents\\GitHub\\safe-js\\server\\save\\pages\\cd5799acbcd45100ffea5ff03da25ef53e72678433193b23d627d8a42ef96844\\36b21df7678e9376d8281aefab4a8baef1ff73972a1e15aa11fb9465ec152f77",
"C:\\Users\\User\\Documents\\GitHub\\safe-js\\server\\save\\pages\\cd5799acbcd45100ffea5ff03da25ef53e72678433193b23d627d8a42ef96844\\e53673684f785145b51d8fdbcfd63b90e25557e6ea9ef99a39ae84763f3f764a"

hehe=  [
    "C:\\Users\\User\\Documents\\GitHub\\safe-js\\server\\save\\pages\\cd5799acbcd45100ffea5ff03da25ef53e72678433193b23d627d8a42ef96844\\4bf4394656514a89b35920553248e66850e96bee64843d289c7bfcb868f8f856",
]

fldr = "C:\\Users\\User\\Documents\\GitHub\\safe-js\\server\\save\\js_dynamic_results"

# for x in hehe:
#     print('\\'.join(x.split('\\')[-2:]))
#     res =  run_command("box-js {} --no-shell-error --no-folder-exists --output-dir {}".format(x, fldr))



# print(entropy("hello"))

# x = "C:\\\\Users\\\\User\\\\Documents\\\GitHub\\safe-js\\sample1.txt"


# res = run_command("box-js {} --no-shell-error --no-folder-exists --output-dir {}".format(x, fldr))

# import re

# PATTERN = r".+search\(.+\)"

# file_data = get_file_buffer("C:\\Users\\User\\Desktop\\testfind.txt")


# res = re.findall(PATTERN, file_data)
# for x in res:
#     print(x)
# print("res: ", res)
