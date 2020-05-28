import re
from error_categories_EE2 import add_category

def filter_tuple(error_dictionary, error, regex_pat, sub_sym):
    err_prefix = "_NULL_"
    # Error can be empty tuple
    if len(error) == 2:
        error_dictionary["err_prefix"] = err_prefix
        error_dictionary["error"] = "_NULL_"
        error_dictionary["category"] = "_NULL_"
        return error_dictionary
    elif 'No such file or directory' in error:
        error = error[1:-1].strip()
        err_prefix = "No such file or directory"
    else:
        prefix = re.split(regex_pat, error)
        prefix = list(filter(lambda s: any([c.isalnum() for c in s]), prefix))[0]
        err_prefix = re.sub(sub_sym, '', prefix).replace("(", ' ').replace("[", '').replace("]", '').strip()
        # Update error dictionary for error and append to logs
    error_dictionary["error"] = error
    error_dictionary["err_prefix"] = err_prefix
    category = add_category(error_dictionary)
    error_dictionary["category"] = category
    return error_dictionary
