import re
from filter_single_quote import filter_single
from filter_double_quote import filter_double
from filter_noquote_tuple import filter_tuple

def filter_error(error, errlog_dictionary):
    """Filter_error allocates a certain filter based on the format of the error coming from EE2. Error from our system have no standard and are generally chaotic and messy.
    As such, an error can be double quotes, single quotes or a tuple. Depending on how the error is wrapped this functions send it to one of the helper functions."""
    # Initiate format variables
    delimiters = "{", "}", "''", ":", ",", "message"
    regex_pattern = '|'.join(map(re.escape, delimiters))
    symbols_to_sub = r'([\'"{}\\><*])'
    #Base Case
    if not error:
        errlog_dictionary["error"] = "_NULL_"
        errlog_dictionary["err_prefix"] = "_NULL_"
        errlog_dictionary["category"] = "_NULL_"
    # Filter defined per error format
    elif error[0] == error[-1] == "'":
        errlog_dictionary = filter_single(errlog_dictionary, error, regex_pattern, symbols_to_sub)
    elif error[0] == error[-1] == '"':
        errlog_dictionary = filter_double(errlog_dictionary, error, regex_pattern, symbols_to_sub)
    else:
        errlog_dictionary = filter_tuple(errlog_dictionary, error, regex_pattern, symbols_to_sub)
    return errlog_dictionary
