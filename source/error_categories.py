
import categories_to_error_dictionary

def add_category(app_log):
    app_status = app_log.get('status')
    categories = categories_to_error_dictionary.categories_to_errors_dict()
    for category, error_array in categories.items():
        if isinstance(error_array[0], str):
            for x in error_array:
                if app_status.find(x) >= 0:
                    return category
        elif isinstance(error_array[0], list):
            for lst in error_array:
                for str_error in lst:
                    if app_status.find(str_error) >= 0:
                        return category
    category = app_log.get('method')
    return category
