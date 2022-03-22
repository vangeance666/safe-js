import os

JS_RESERVED_WORDS_PATH = os.path.join(os.getcwd(), "analyzer" , "resources", "reserved_words.txt")
# "C:\Users\User\Documents\GitHub\safe-js\server\analyzer\resources\reserved_words.txt"

PAGE_SAVE_FLDR = os.path.join(os.getcwd(), "data", "pages")


# "data\\js_dynamic_results\\<js_src_hash"
DYNAMIC_DUMP_FLDR = os.path.join(os.getcwd(), "data", "js_dynamic_results")

RESULTS_SAVED_PATH = os.path.join(os.getcwd(), "save",  "database.pickle")
