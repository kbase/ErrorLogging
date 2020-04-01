
import categories_to_error_dictionary

def add_category(app_log):
    """ Add category function searches the app's error log for certain substrings.
    Each of the substrings maps to a specific category of error.
    Once a substring is found the error log a category is returned
     Otherwise, if no mapping is found, the app method name is given as the error category"""
    # Pull app log and get error -> categories dictionary
    app_status = app_log.get('status')
    categories = categories_to_error_dictionary.categories_to_errors_dict()
    for category, error_array in categories.items():
        # Dictionary values can be either an array of strings or an array of lists
        # Check instance of error array
        if isinstance(error_array[0], str):
            for x in error_array:
                # If error substring found in app log; category is returned
                if app_status.find(x) >= 0:
                    return category
        elif isinstance(error_array[0], list):
            for lst in error_array:
                for str_error in lst:
                    if app_status.find(str_error) >= 0:
                        return category
    # If error log does not match any known mapping, the category
    # is given as the app method name
    category = app_log.get('method')
    return category
