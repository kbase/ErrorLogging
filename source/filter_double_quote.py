import re
import ast
from error_categories_EE2 import add_category


def filter_double(error_dictionary, error, regex_pat, sub_sym):
    """Filter double filters errors that are double quoted. This double quoted error can be "''",  "()" or other"""
    # First the other quotes are striped
    error = error[1:-1].strip()
    # Errors that end in double quotes can be wrapping single quotes
    if error[0] == error[-1] == "'":
        error = error[1:-1]
        # The 'error prefix' is simply a cleaned version of the original error
        prefix = re.split(regex_pat, error)
        prefix = list(filter(lambda s: any([c.isalnum() for c in s]), prefix))[0]
        err_prefix = re.sub(sub_sym, '', prefix).replace("(", ' ').replace("[", '').strip()
    # Error can be tuple wrapped in string
    elif error[0] == '(':
        error_tuple = ast.literal_eval(str(error))
        # When error is wrapped in a tuple the first element is usually a number and the second tuple element is the error message
        err_prefix = error_tuple[1]
        # Had issues of errors being of type bytes
        if isinstance(err_prefix, (bytes)):
            err_prefix = str(err_prefix)
        if isinstance(error, (bytes)):
            error = str(error)
    else:
        prefix = re.split(regex_pat, error)
        prefix = list(filter(lambda s: any([c.isalnum() for c in s]), prefix))[0]
        err_prefix = re.sub(sub_sym, '', prefix).replace("(", ' ').replace("[", '').replace("]", '').strip()
    # The full original error (in string format) is put in the dictionary under error
    error_dictionary["error"] = error
    # The 'error_prefix' is in fact the neat and condensed form of the full error
    error_dictionary["err_prefix"] = err_prefix
    # Once the error and error_prefix is in the dictionary, the dictionary is sent to add_category for a category to be added
    category = add_category(error_dictionary)
    error_dictionary["category"] = category
    return error_dictionary
