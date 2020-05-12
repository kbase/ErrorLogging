import re
from filter_single_quote import filter_single
from filter_double_quote import filter_double
from filter_noquote_tuple import filter_tuple

def filter_error(error, errlog_dictionary, log):
    # Initiate format variables
    delimiters = "{", "}", "''", ":", ",", "message"
    regex_pattern = '|'.join(map(re.escape, delimiters))
    symbols_to_sub = r'([\'"{}\\><*])'
    regexPattern = '|'.join(map(re.escape, delimiters))
    #Base Case
    if not error:
        errlog_dictionary["error"] = "_NULL_"
        errlog_dictionary["err_prefix"] = "_NULL_"
        errlog_dictionary["category"] = "_NULL_"
    # Filter defined per error format
    elif error[0] == error[-1] == "'":
        errlog_dictionary = filter_single(errlog_dictionary, error, regex_pattern, symbols_to_sub, log)
    elif error[0] == error[-1] == '"':
        errlog_dictionary = filter_double(errlog_dictionary, error, regex_pattern, symbols_to_sub, log)
    else:
        errlog_dictionary = filter_tuple(errlog_dictionary, error, regex_pattern, symbols_to_sub, log)
    return errlog_dictionary
          
