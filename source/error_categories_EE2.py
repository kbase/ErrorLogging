

from config_to_error_dictionaries import config_to_dictionary


def add_category(error_dict):
    """ Add category function searches the app's error log for certain substrings.
    Each of the substrings maps to a specific category of error.
    Once a substring is found the error log a category is returned
    Otherwise, if no mapping is found, the app method name is given as the error category"""
    # Pull app log and get error -> categories dictionary
    if isinstance(error_dict['error'], str):
        error_values_all = error_dict['error'] + error_dict['traceback']
    else:
        error_values_all = error_dict['traceback']
    # Categories is a helper function that takes the category listing the Error.ini and returns a dict from key to category
    categories = config_to_dictionary()
    for category, error_array in categories.items():
        # Dictionary values can be either an array of strings or an array of lists
        for x in error_array:
            if x in error_values_all:
                # If error substring found category is returned
                return category
    # If error log does not match any known mapping, the category
    # is given as the app method name
    category = error_dict['app_id']
    return category
