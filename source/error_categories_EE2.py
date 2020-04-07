
import categories_to_error_dictionary

def add_category(error_dict):
    """ Add category function searches the app's error log for certain substrings.
    Each of the substrings maps to a specific category of error.
    Once a substring is found the error log a category is returned
    Otherwise, if no mapping is found, the app method name is given as the error category"""
    # Pull app log and get error -> categories dictionary
    error_values_all = error_dict['error'] + error_dict['traceback']
    categories = categories_to_error_dictionary.categories_to_errors_dict()
    for category, error_array in categories.items():
        # Dictionary values can be either an array of strings or an array of lists
        # Check instance of error array
        if isinstance(error_array[0], str):
            for x in error_array:
                if x in error_values_all:
                    # If error substring found category is returned
                    return category
        elif isinstance(error_array[0], list):
            for lst in error_array:
                for str_error in lst:
                    if str_error in error_values_all:
                        return category
    # If error log does not match any known mapping, the category
    # is given as the app method name
    category = error_dict['app_id']
    return category
