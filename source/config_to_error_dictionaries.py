import configparser
config = configparser.ConfigParser()

def config_to_dictionary():
    """Config_to_dictionaries is a simple function, that takes the error category list (Errors.ini) and converts it to a dictionary format.
    Each key in the dictionary is a 'section' from Errors.ini. For each section-errors entry is added to the larger error_dictionary/error_category_dictionary through an update"""
    config.read('Errors.ini')
    error_dictionary = {}
    key_list = config.sections()
    for section in key_list:
        errors = list(dict(config.items(section)).values())
        app_dictionary = {section: errors}
        error_dictionary.update(app_dictionary)
    return error_dictionary
