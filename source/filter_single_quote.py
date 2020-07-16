import re
from error_categories_EE2 import add_category

def filter_single(error_dictionary, error, regex_pat, sub_sym):
    """Filter_single filters errors wrapped in single quotes. Ideally all errors should have this simple format from the json log"""
    if len(error) == 2:
        error_dictionary["error"] = "_NULL_"
        error_dictionary["err_prefix"] = "_NULL_"
        error_dictionary["category"] = "_NULL_"
    else:
        error = error[1:-1].strip()
        prefix = re.split(regex_pat, error)
        prefix = list(filter(lambda s: any([c.isalnum() for c in s]), prefix))[0]
        err_prefix = re.sub(sub_sym, '', prefix).replace("(", ' ').replace("[", '').strip()
        error_dictionary["error"] = error
        error_dictionary["err_prefix"] = err_prefix
        category = add_category(error_dictionary)
        error_dictionary["category"] = category
        return error_dictionary
