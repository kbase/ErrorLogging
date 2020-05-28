import re
import ast
from error_categories_EE2 import add_category


def filter_double(error_dictionary, error, regex_pat, sub_sym):
    error = error[1:-1].strip()
    # Errors that end in double quotes can be wrapping single qoutes
    if error[0] == error[-1] == "'":
        error = error[1:-1]
        prefix = re.split(regex_pat, error)
        prefix = list(filter(lambda s: any([c.isalnum() for c in s]), prefix))[0]
        err_prefix = re.sub(sub_sym, '', prefix).replace("(", ' ').replace("[", '').strip()
    # Error can be tuple wrapped in string
    elif error[0] == '(':
        error_tuple = ast.literal_eval(str(error))
        err_prefix = error_tuple[1]
        if isinstance(err_prefix, (bytes)):
            err_prefix = str(err_prefix)
        if isinstance(error, (bytes)):
            error = str(error)
    else:
        prefix = re.split(regex_pat, error)
        prefix = list(filter(lambda s: any([c.isalnum() for c in s]), prefix))[0]
        err_prefix = re.sub(sub_sym, '', prefix).replace("(", ' ').replace("[", '').replace("]", '').strip()

    error_dictionary["error"] = error
    error_dictionary["err_prefix"] = err_prefix
    category = add_category(error_dictionary)
    error_dictionary["category"] = category
    return error_dictionary
