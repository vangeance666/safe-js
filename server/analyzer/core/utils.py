import os
import importlib
import inspect
import pkgutil

def enumerate(dirpath, module_prefix, namespace, class_,
                      attributes={}, as_dict=False):
    
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

def read_in_chunks(file_object, chunk_size=1024):
    while True:
        data = file_object.read(chunk_size)
        if not data:
            break
        yield data

def get_file_buffer(file_path):

    with open(file_path, 'r') as f:
        return f.read()
    
    # with open(file_path, 'r') as f:
    #     for piece in read_in_chunks(f):
    #         yield piece

import re

PATTERN = r".+search\(.+\)"

file_data = get_file_buffer("C:\\Users\\User\\Desktop\\testfind.txt")


res = re.findall(PATTERN, file_data)
for x in res:
    print(x)
print("res: ", res)
