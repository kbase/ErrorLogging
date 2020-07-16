import re
from error_categories_EE2 import add_category

def filter_tuple(error_dictionary, error, regex_pat, sub_sym):
    """Filter_tuple filters errors that are wrapped in tuples"""
    err_prefix = "_NULL_"
    # Error can be empty tuple
    if len(error) == 2:
        error_dictionary["err_prefix"] = err_prefix
        error_dictionary["error"] = "_NULL_"
        error_dictionary["category"] = "_NULL_"
        return error_dictionary
    # Error can be 'no such file or directory' error in either the first or second position
    elif 'No such file or directory' in error:
        error = error[1:-1].strip()
        err_prefix = "No such file or directory"
    else:
        prefix = re.split(regex_pat, error)
        prefix = list(filter(lambda s: any([c.isalnum() for c in s]), prefix))[0]
        err_prefix = re.sub(sub_sym, '', prefix).replace("(", ' ').replace("[", '').replace("]", '').strip()
    # Update error dictionary for error and append to logs
    # Once the error and error_prefix is in the dictionary, the dictionary is sent to add_category for a category to be added.
    error_dictionary["error"] = error
    error_dictionary["err_prefix"] = err_prefix
    category = add_category(error_dictionary)
    error_dictionary["category"] = category
    return error_dictionary
