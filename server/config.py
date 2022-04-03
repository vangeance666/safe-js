import os

JS_RESERVED_WORDS_PATH = os.path.join(os.getcwd(), "analyzer" , "resources", "reserved_words.txt")

PAGE_SAVE_FLDR = os.path.join(os.getcwd(), "data", "pages")

DYNAMIC_DUMP_FLDR = os.path.join(os.getcwd(), "data", "js_dynamic_results")

ANALYZED_PAGES_SAVE_PATH = os.path.join(os.getcwd(), "save",  "database.pickle")
PENDING_PAGES_SAVE_PATH = os.path.join(os.getcwd(), "save", "pending.pickle")


ERROR_DUMP_PATH = os.path.join(os.getcwd(), "save", "errors")